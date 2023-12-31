from fastapi import FastAPI, HTTPException, Request, Form
from schemas.bot_alert import BotAlert
from config.db import con
from models.index import bot_alert as model_bot_alert
from models.okx_user import okx_users as model_okx_user
from okx_trading import OkxPlaceOrder
from fastapi.templating import Jinja2Templates

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
        okx_place_order_result = OkxPlaceOrder.place_order(
            botalert=botalert
        )
        # bybit_place_order_result = BybitPlaceOrder.place_order(
        #     botalert=botalert
        # )
        con.commit()

        # Check if the data was inserted and the order was placed successfully
        if data.is_insert and okx_place_order_result:  # Update with the appropriate
            return {'status': 'success'}
        else:
            raise HTTPException(status_code=500, detail='Failed to insert data into the database or place order')
    except Exception as e:
        # Handle exceptions and provide appropriate error response
        return {'status': 'fail', 'error_message': str(e)}
