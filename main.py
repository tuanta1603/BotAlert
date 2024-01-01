from fastapi import FastAPI, HTTPException, Request, Form
from schemas.bot_alert import BotAlert
from config.db import con
from models.index import bot_alert as model_bot_alert
from models.okx_user import okx_users as model_okx_user
from okx_trading import OkxPlaceOrder
from fastapi.templating import Jinja2Templates
from sqlalchemy import select
import asyncio

from bybit_trading import BybitPlaceOrder


templates = Jinja2Templates(directory="templates")
app = FastAPI()


@app.get('/')
async def home(request: Request):
    return templates.TemplateResponse('index.html', {'request': request})


@app.post("/add_okx")
async def submit_okx_form(
    api_key: str = Form(...),
    secret_key: str = Form(...),
    code: str = Form(...),
    total_balance: str = Form(...),
    min_slot_play: str = Form(...),
):
    try:
        # Insert data into the database
        data = con.execute(model_okx_user.insert().values(
            api_key=api_key,
            secret_key=secret_key,
            passphrase=code,
            total_balance=int(total_balance),
            min_slot_play=int(min_slot_play),
            status=1
        ))
        con.commit()

        # Check if the data was inserted successfully
        if data.is_insert:  # Update with the appropriate condition
            return {'status': 'success', 'message': 'Data inserted successfully'}
        else:
            raise HTTPException(status_code=500, detail='Failed to insert data into the database or place order')
    except ValueError:
        raise HTTPException(status_code=422, detail='Invalid value for total_balance. Must be an integer.')
    except Exception as e:
        # Handle exceptions and provide appropriate error response
        return {'status': 'fail', 'error_message': str(e)}


@app.post('/api/bot_alert')
async def create_bot_alert(botalert: BotAlert):
    try:
        print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
        # Select data from the okx_users table
        users_data = con.execute(select(model_okx_user.columns).where(model_okx_user.c.status == 1)).fetchall()
        if not users_data:
            raise HTTPException(status_code=404, detail='User not found')
        # Insert data into the database
        data = con.execute(model_bot_alert.insert().values(
            syminfo=botalert.syminfo,
            prefix=botalert.prefix,
            ticker=botalert.ticker,
            basecurrency=botalert.basecurrency,
            currency=botalert.currency,
            timeframe=botalert.timeframe,
            side=botalert.side,
            position=botalert.position,
            Action=botalert.Action,
            prices_pos=botalert.prices_pos,
            prices_tp=botalert.prices_tp,
            precent_tp=botalert.precent_tp,
            pos_leverage=botalert.pos_leverage,
            pos_currency=botalert.pos_currency,
            pos_quantity=botalert.pos_quantity,
            CurrencyManual=botalert.CurrencyManual,
            QuantityManual=botalert.QuantityManual,
            codename=botalert.codename,
            type=botalert.type
        ))

        async def place_order_for_user(user_data):
            try:
                result = await OkxPlaceOrder.place_order(
                    botalert=botalert,
                    apikey=user_data.api_key,
                    secretkey=user_data.secret_key,
                    passphrase=user_data.passphrase,
                    total_balance=user_data.total_balance,
                    min_slot_play=user_data.min_slot_play
                )
                return {'user_id': user_data.id, 'result': result, 'error_message': None}
            except Exception as e:
                return {'user_id': user_data.id, 'result': None, 'error_message': str(e)}

        # Use asyncio.gather to execute the asynchronous functions concurrently
        # Use asyncio.gather to execute the asynchronous functions concurrently
        results = await asyncio.gather(*(place_order_for_user(user_data) for user_data in users_data))

        con.commit()

        # Check if the data was inserted and the orders were placed successfully
        if data.is_insert and all(result['result'] for result in results if result):
            user_results = {result['user_id']: result['result'] for result in results if result}
            return {'status': 'success', 'results': user_results}
        else:
            errors = [result['error_message'] for result in results if result and result['error_message']]
            raise HTTPException(status_code=500,
                                detail=f'Failed to insert data into the database or place order. Errors: {errors}')

    except Exception as e:
        # Handle exceptions and provide appropriate error response
        return {'status': 'fail', 'error_message': str(e)}

