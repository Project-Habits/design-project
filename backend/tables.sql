-- Database: projhabits
DROP TABLE IF EXISTS users CASCADE;
DROP TABLE IF EXISTS meals CASCADE;
DROP TABLE IF EXISTS workouts CASCADE;
DROP TABLE IF EXISTS user_meals CASCADE;
DROP TABLE IF EXISTS user_workouts CASCADE;
DROP TABLE IF EXISTS activities CASCADE;

CREATE table users (
	uid INT Primary Key,
	username VARCHAR(50),
	u_password VARCHAR(20));
	
CREATE TABLE meals (
	mid INT PRIMARY KEY,
	mealname VARCHAR(30),
	calories INT,
	m_type CHAR(1));
	
CREATE TABLE workouts (
	wid INT,
	workoutname VARCHAR(30),
	calories_burned INT,
	w_type CHAR(1),
	PRIMARY KEY(wid));

CREATE TABLE user_meals (
	uid INT REFERENCES users(uid),
	mid INT REFERENCES meals(mid),
	PRIMARY KEY (uid, mid));
	
CREATE TABLE user_workouts (
	uid INT REFERENCES users(uid),
	wid INT REFERENCES workouts(wid),
	PRIMARY KEY (uid, wid));

CREATE TABLE activities(
	activity_id INT,
	uid INT REFERENCES users(uid),
	mid INT REFERENCES meals(mid),
	wid INT REFERENCES workouts(wid),
	a_day DATE,
	PRIMARY KEY (activity_id, uid)
);