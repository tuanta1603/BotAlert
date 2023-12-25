from config.db import meta
from sqlalchemy import Column, Table
from sqlalchemy.sql.sqltypes import Integer, String, DateTime

bot_alert = Table(
    'bot_alert', meta,
    Column('id', Integer, primary_key=True),
    Column('syminfo', String(255)),
    Column('prefix', String(255)),
    Column('ticker', String(255)),
    Column('basecurrency', String(255)),
    Column('currency', String(255)),
    Column('timeframe', String(255)),
    Column('side', String(255)),
    Column('position', String(255)),
    Column('Action', String(255)),
    Column('prices_pos', String(255)),
    Column('prices_tp', String(255)),
    Column('precent_tp', String(255)),
    Column('pos_leverage', String(255)),
    Column('pos_currency', String(255)),
    Column('pos_quantity', String(255)),
    Column('CurrencyManual', String(255)),
    Column('QuantityManual', String(255)),
    Column('codename', String(255)),
    Column('type', String(255)),

)
