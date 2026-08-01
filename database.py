from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base,sessionmaker

#DATABASE_URL = "mysql+pymysql://root:Vasavi%40572@localhost:3306/restaurant_db"
DATABASE_URL ="mysql+pymysql://avnadmin:AVNS_mw4f0Fy7CB9EF4UP2TI@vasavi-project-vasavireddy2006-4319.g.aivencloud.com:23340/defaultdb?"
engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False
)

Base = declarative_base()
