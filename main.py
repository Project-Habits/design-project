import bottle
from pydantic import BaseModel
from bottle import response
from bottle_postgresql import Configuration, Database
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.ext.asyncio import AsyncSession

SQLALCHEMY_DATABASE_URL = "postgresql://postgres:playerubg209@localhost/projhabits"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

async def get_db():
    session = AsyncSession(engine)
    try:
        yield session
    finally:
        await session.close()


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    hashed_password = Column(String)


class Recs(BaseModel):
    username: str
    workout: str
    meal: str

configuration_dict = {
    'connect_timeout': 10,
    'dbname': 'projhabits',
    'host': 'localhost',
    'password': 'playerubg209',     # insert db password
    'port': 5435,       # insert port number here
    'user': 'postgres'
}

configuration = Configuration(configuration_dict=configuration_dict)
def connect():
    return Database(configuration)

class EnableCors(object):
    name = 'enable_cors'
    api = 2

    def apply(self, fn, context):
        def _enable_cors(*args, **kwargs):
            # set CORS headers
            response.headers['Access-Control-Allow-Origin'] = '*'
            response.headers['Access-Control-Allow-Methods'] = 'GET, POST, PUT, OPTIONS'
            response.headers['Access-Control-Allow-Headers'] = 'Origin, Accept, Content-Type, X-Requested-With, X-CSRF-Token'

            if bottle.request.method != 'OPTIONS':
                # actual request; reply with the actual response
                return fn(*args, **kwargs)

        return _enable_cors


app = bottle.app()

@app.route('/', method=['OPTIONS', 'GET'])
def lvambience():
    response.headers['Content-type'] = 'application/json'
    # logging.debug('reached')
    # print('reached again')
    print('landed')
    # test to see if it writes to db --- it does

    return '[1]'

@app.post("/")
def return_status():
    print('returned')
    myDict = {
    'workout': { "Bench Press": "3x10", "Military Press": "3x10", "Squats": "3x8" }, 'meal': { "Name": "Chicken and Rice dinner", "Link": "https://www.campbells.com/recipes/15-minute-chicken-rice-dinner/" }
    }
    with connect() as connection:
        (
            connection
            .insert('meals')
            .set('uid', 1)
            .set('mid', 1)
            .set('mealname', myDict['meal']['Name'])
            .set('calories', 1400)
            .execute()   
        )
    with connect() as connection:
        (
            connection
            .insert('workouts')
            .set('uid', 1)
            .set('wid', 1)
            .set('workoutname', 'Bench Press') # Need to create field for workout name
            .set('calories_burned', 400)
            .execute()   
        )
    return myDict

@app.post("/login")
def get_user():
    print('logging in...')
    with connect() as connection:
        (
            connection
            .execute('SELECT uid FROM users WHERE uid = {}'.format(1))
        )

app.install(EnableCors())

app.run(port=8000)