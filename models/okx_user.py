from config.db import meta
from sqlalchemy import Column, Table
from sqlalchemy.sql.sqltypes import Integer, String, DateTime

okx_users = Table(
    'okx_users', meta,
    Column('id', Integer, primary_key=True),
    Column('api_key', String(255)),
    Column('secret_key', String(255)),
    Column('passphrase', String(255)),
    Column('total_balance', Integer),
    Column('min_slot_play', Integer),
    Column('status', Integer),

)
