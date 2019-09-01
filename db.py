import datetime
import os

from sqlalchemy import Column, DateTime, Integer, MetaData, Table, Text
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

default_uri = 'postgresql+psycopg2://user:pw@localhost:5432/foo'

db_uri = os.environ.get('DB_URI', default_uri)

engine = create_engine(db_uri, echo=True)
session = scoped_session(
    sessionmaker(
        autocommit=False,
        autoflush=False,
        bind=engine
    )
)

metadata = MetaData()

widgets = Table(
    'widgets',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('foo', Text),
    Column('bar', DateTime, default=datetime.datetime.utcnow)
)

metadata.create_all(engine)
#   NOTE(andy): uncomment to remove errors!
# engine.dispose()
