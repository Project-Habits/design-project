from sqlalchemy import Column, DateTime, ForeignKey, Integer, PrimaryKeyConstraint, String, Float, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

Base  = declarative_base()

class User(Base):
    __tablename__ = 'users'
    uid  = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    u_password = Column(String)

class Meal(Base):
    __tablename__ = 'meals'
    mid = Column(Integer, primary_key=True)
    mealname = Column(String)
    calories = Column(Integer)
    m_type = Column(String)
    diet_type = Column(String)
    link = Column(String)

class Workout(Base):
    __tablename__ = 'workouts'
    wid = Column(Integer, primary_key=True)
    workoutname = Column(String)
    calories_burned = Column(Integer)
    w_type = Column(String)
    section = Column(String)

class User_Meal(Base):
    __tablename__ = 'user_meals'
    uid = Column(Integer, ForeignKey('users.uid'))
    mid = Column(Integer, ForeignKey('meals.mid'))
    __table_args__ = (
        PrimaryKeyConstraint(uid, mid),
        {},
    )
    
class User_Workout(Base):
    __tablename__ = 'user_workouts'
    uid = Column(Integer, ForeignKey('users.uid'))
    wid = Column(Integer, ForeignKey('workouts.wid'))
    __table_args__ = (
        PrimaryKeyConstraint(uid, wid),
        {},
    )

class Activity(Base):
    __tablename__ = 'activities'
    activity_id = Column(Integer, primary_key=True)
    uid = Column(Integer, ForeignKey('users.uid'))
    mid = Column(Integer, ForeignKey('meals.mid'))
    wid = Column(Integer, ForeignKey('workouts.wid'))
    a_day = Column(Date)
