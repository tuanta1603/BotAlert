from fastapi import FastAPI, HTTPException
from schemas.bot_alert import BotAlert
from config.db import con
from models.index import bot_alert as model_bot_alert
from okx_trading import PlaceOrder
# from okx.PlaceOrder import place_order

app = FastAPI()


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
        place_order_result = PlaceOrder.place_order(
            botalert=botalert
        )
        con.commit()

        # Check if the data was inserted and the order was placed successfully
        if data.is_insert and place_order_result:  # Update with the appropriate condition
            return {'status': 'success'}
        else:
            raise HTTPException(status_code=500, detail='Failed to insert data into the database or place order')
    except Exception as e:
        # Handle exceptions and provide appropriate error response
        return {'status': 'fail', 'error_message': str(e)}
