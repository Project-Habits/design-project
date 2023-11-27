-- Insert data into users table
INSERT INTO users (uid, username, u_password) VALUES
(1, 'user1', 'pass1'),
(2, 'user2', 'pass2'),
(3, 'user3', 'pass3'),
(4, 'user4', 'pass4'),
(5, 'user5', 'pass5'),
(6, 'user6', 'pass6'),
(7, 'user7', 'pass7'),
(8, 'user8', 'pass8');

-- Insert data into meals table
INSERT INTO meals (mid, mealname, calories, m_type, diet_type, link) VALUES
(1, 'Savory Crepes', 400, 'b', 'Balanced', 'http://example.com/breakfast'),
(2, 'Huevos Pericos', 600, 'b', 'Vegetarian', 'http://example.com/lunch'),
(3, 'Guacamole on Tostada', 800, 'b', 'Vegan', 'http://example.com/dinner'),
(4, 'Cucumber Salad', 1000, 'l', 'Balanced', 'http://example.com/snack1'),
(5, 'Banana', 150, 'l', 'Vegetarian', 'http://example.com/snack2'),
(6, 'Asian Avocado', 450, 'l', 'Vegan', NULL),
(7, 'Avocado Chicken Salad', 700, 'd', 'Balanced', NULL),
(8, 'Chopped Salad', 550, 'd', 'Vegetarian', 'http://example.com/meal8'),
(9, 'Vegetarian Fajita Pasta', 1500, 'd', 'Vegan', 'http://example.com/bingbong'),
(10, '2 Bananas', 2000, 'b', 'Balanced', 'http://example.com/breakfast'),
(11, 'Brie and Celery', 2000, 'b', 'Vegetarian', 'http://example.com/lunch'),
(12, 'Spinach Tomato Salad', 2000, 'l', 'Vegan', 'http://example.com/dinner'),
(13, 'Tuna Apple Salad', 2000, 'd', 'Balanced', 'http://example.com/snack1'),
(14, 'Pickle and Cheddar Sandwich', 2300, 'b', 'Vegetarian', 'http://example.com/snack2'),
(15, 'Smashed White Bean', 2450, 'l', 'Vegan', NULL),
(16, 'Green Bean Tuna', 2700, 'l', 'Balanced', NULL),
(17, 'Thai Cucumber Salad', 2550, 'd', 'Vegetarian', 'http://example.com/meal8'),
(18, 'Rice and Beans', 2500, 'd', 'Vegan', 'http://example.com/bingbong');

-- Insert data into workouts table
INSERT INTO workouts (wid, workoutname, calories_burned, w_type, section) VALUES
(1, 'Bench Press', 300, 'S', 'Chest'),
(2, 'Bicep Curls', 400, 'S', 'Biceps'),
(3, 'Rowing', 150, 'S', 'Back'),
(4, 'Push ups', 500, 'S', 'Shoulders'),
(5, 'Cycling', 350, 'C', 'Cardio'),
(6, 'Running', 200, 'C', 'Cardio'),
(7, 'Walking', 50, 'C', 'Cardio'),
(8, 'HIIT', 500, 'C', 'Cardio'),
(9,'Dumbbell Flys', NULL, 'S', 'Chest'),
(10,'Shoulder Press', NULL, 'S', 'Shoulders'),
(11,'Pull Ups', NULL, 'S', 'Back'),
(12,'Back Extension', NULL, 'S', 'Back'),
(13,'Skull Crushers', NULL, 'S', 'Triceps'),
(14,'Tricep Pushdown', NULL, 'S', 'Triceps'),
(15,'Standing Leg Raises', NULL, 'S', 'Abs'),
(16,'Dead Bug', NULL, 'S', 'Abs'),
(17, 'Calf Raises', NULL, 'S', 'Calves'),
(18, 'Leg Curls', NULL, 'S', 'Hamstrings'),
(19, 'Goblet Squats', NULL, 'S', 'Quads'),
(20, 'RDLs', NULL, 'S', 'Hamstrings'),
(21, 'Leg Press', NULL, 'S', 'Quads'),
(22, 'Hip Thrust', NULL, 'S', 'Glutes'),
(23, 'Sumo Squats', NULL, 'S', 'Glutes'),
(24, 'Jump Rope', NULL, 'C', 'Cardio'),
(25, 'Burpees', NULL, 'C', 'Cardio'),
(26, 'Mountain Climbers', NULL, 'C', 'Cardio');

-- Insert data into user_meals table
INSERT INTO user_meals (uid, mid) VALUES
(1, 2),
(1, 5),
(2, 3),
(3, 1),
(4, 4),
(5, 6),
(6, 7),
(7, 8),
(8, 4),
(1, 12),
(7, 13),
(3, 10),
(5, 4),
(1, 18);

-- Insert data into user_workouts table
INSERT INTO user_workouts (uid, wid) VALUES
(1, 2),
(2, 3),
(3, 1),
(4, 5),
(5, 4),
(6, 6),
(7, 8),
(8, 7);

-- Insert data into activities table
INSERT INTO activities (activity_id, uid, mid, wid, a_day) VALUES
(1, 1, 2, 2, '2023-01-01'),
(2, 2, 3, 3, '2023-01-02'),
(3, 3, 1, 1, '2023-01-03'),
(4, 4, 4, 5, '2023-01-04'),
(5, 5, 6, 6, '2023-01-05'),
(6, 6, 7, 8, '2023-01-06'),
(7, 7, 8, 7, '2023-01-07'),
(8, 8, 4, 4, '2023-01-08'),
(9, 1, 12, 3, '2023-01-09');
