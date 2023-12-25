from fastapi import FastAPI
from schemas.bot_alert import BotAlert
from config.db import con
from models.index import bot_alert as model_bot_alert

app = FastAPI()


# @app.get("/")
# async def root():
#     return {"message": "Hello World"}
#
#
# @app.get("/hello/{name}")
# async def say_hello(name: str):
#     return {"message": f"Hello {name}"}


@app.post('/api/bot_alert')
async def create_bot_alert(botalert: BotAlert):
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

    if data.is_insert:
        return {
            'status': 'success',
        }
    else:
        return {
            'status': 'fail',
        }
