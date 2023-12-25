from pydantic import BaseModel


class BotAlert(BaseModel):
    syminfo: str
    prefix: str
    ticker: str
    basecurrency: str
    currency: str
    timeframe: str
    side: str
    position: str
    Action: str
    prices_pos: str
    prices_tp: str
    precent_tp: str
    pos_leverage: str
    pos_currency: str
    pos_quantity: str
    CurrencyManual: str
    QuantityManual: str
    codename: str
    type: str
