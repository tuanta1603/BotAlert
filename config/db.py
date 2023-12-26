from sqlalchemy import create_engine, MetaData
engine = create_engine('mysql+pymysql://bingx:Bing@123Login@localhost:3306/bingx')
meta = MetaData()
con = engine.connect()
