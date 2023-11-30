-- =================================
-- MUST RUN `tables.sql` FIRST !!!!!
-- ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

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
-- <1800
-- Balanced
(1, 'Savory Crepes', 503, 'b', 'Balanced', 'https://www.eatthismuch.com/recipe/nutrition/savory-crepes,3837734/'),
(2, 'Cottage Cheese & Apricots', 600, 'b', 'Balanced', 'https://www.eatthismuch.com/recipe/nutrition/cottage-cheese-apricots,3266357/'),
(3, 'Spinach and Poached Egg Muffins', 800, 'b', 'Balanced', 'https://www.eatthismuch.com/recipe/nutrition/spinach-and-poached-egg-muffins,936001/'),
(4, 'Goat Cheese on Toasted Bread with Tomato', 1000, 'b', 'Balanced', 'https://www.eatthismuch.com/recipe/nutrition/goat-cheese-on-toasted-bread-with-tomato,905637/'),
(5, 'Banana/Strawberry Smoothie', 150, 'l', 'Balanced', 'https://www.eatthismuch.com/recipe/nutrition/sunrise-smoothie,939657/'),
(6, 'Bell Pepper and Hummus Snack', 450, 'l', 'Balanced', 'https://www.eatthismuch.com/recipe/nutrition/bell-pepper-and-hummus-snack,3262952/'),
(7, 'Cucumber Salad', 700, 'l', 'Balanced', 'https://www.eatthismuch.com/recipe/nutrition/cucumber-salad,3269222/'),
(8, 'Cilantro Crab & Corn Stuffed Peppers', 550, 'l', 'Balanced', 'https://www.eatthismuch.com/recipe/nutrition/cilantro-crab-corn-stuffed-peppers,334562/'),
(9, 'Avocado Chicken Salad', 1500, 'd', 'Balanced', 'https://www.eatthismuch.com/recipe/nutrition/avocado-chicken-salad,3186597/'),
(10, 'Microwaved Sweet Potato', 1400, 'd', 'Balanced', 'https://www.eatthismuch.com/recipe/nutrition/microwaved-sweet-potato,42621/'),
(11, 'Brazilian Chicken Salad (Salpicão)', 1400, 'd', 'Balanced', 'https://www.eatthismuch.com/recipe/nutrition/brazilian-chicken-salad-salpicao,3194118/'),
(12, 'Edamame Sesame Bowl', 1400, 'd', 'Balanced', 'https://www.eatthismuch.com/recipe/nutrition/edamame-sesame-bowl,208058/'),
-- Vegetarian
(13, 'Microwave Peanut Butter Protein Oats', 2000, 'b', 'Vegetarian', 'https://www.eatthismuch.com/recipe/nutrition/microwave-peanut-butter-protein-oats,1016932/'),
(14, 'Toast with Berries, Basil & Cream Cheese', 2300, 'b', 'Vegetarian', 'https://www.eatthismuch.com/recipe/nutrition/toast-with-berries-basil-cream-cheese,331899/'),
(15, 'Huevos Pericos', 2450, 'b', 'Vegetarian', 'https://www.eatthismuch.com/recipe/nutrition/huevos-pericos,1472994/'),
(16, 'Toast with Tomato and Hummus', 2700, 'b', 'Vegetarian', 'https://www.eatthismuch.com/recipe/nutrition/toast-with-tomato-and-hummus,906348/'),
(17, 'Fruity Almond and Yogurt Smoothie', 2550, 'l', 'Vegetarian', 'https://www.eatthismuch.com/recipe/nutrition/fruity-almond-and-yogurt-smoothie,927220/'),
(18, 'Banana', 2500, 'l', 'Vegetarian', 'https://www.eatthismuch.com/recipe/nutrition/banana,474253/'),
(19, 'Pinto Bean salad', 1000, 'l', 'Vegetarian', 'https://www.eatthismuch.com/recipe/nutrition/pinto-bean-salad,1011211/'),
(20, 'Cauliflower and Tahini', 1000, 'l', 'Vegetarian', 'https://www.eatthismuch.com/recipe/nutrition/cauliflower-and-tahini,3263841/'),
(21, 'Coconut Green Curry and Soba', 1000, 'd', 'Vegetarian', 'https://www.eatthismuch.com/recipe/nutrition/coconut-green-curry-and-soba,203490/'),
(22, 'Chopped Salad', 1000, 'd', 'Vegetarian', 'https://www.eatthismuch.com/recipe/nutrition/chopped-salad,3256074/'),
(23, 'Teriyaki Chickpeas', 1000, 'd', 'Vegetarian', 'https://www.eatthismuch.com/recipe/nutrition/teriyaki-chickpeas,3231755/'),
(24, 'Lebanese Fresh Thyme Tomato Salad', 1000, 'd', 'Vegetarian', 'https://www.eatthismuch.com/recipe/nutrition/lebanese-fresh-thyme-tomato-salad,907074/'),
-- Vegan
(25, 'Chocolate Almond Iced Coffee', 1000, 'b', 'Vegan', 'https://www.eatthismuch.com/recipe/nutrition/chocolate-almond-iced-coffee,907034/'),
(26, 'No-Bake Apple Cookies', 1000, 'b', 'Vegan', 'https://www.eatthismuch.com/recipe/nutrition/no-bake-apple-cookies,906715/'),
(27, 'Peanut Butter & Banana Oatmeal', 1000, 'b', 'Vegan', 'https://www.eatthismuch.com/recipe/nutrition/peanut-butter-banana-oatmeal,413007/'),
(28, 'Guacamole on Tostada', 1000, 'b', 'Vegan', 'https://www.eatthismuch.com/recipe/nutrition/guacamole-on-tostada,906590/'),
(29, 'Vegan Banana Oat Soy Shake', 1000, 'l', 'Vegan', 'https://www.eatthismuch.com/recipe/nutrition/vegan-banana-oat-soy-shake,906806/'),
(30, 'Asian Avocado', 1000, 'l', 'Vegan', 'https://www.eatthismuch.com/recipe/nutrition/asian-avocado,36683/'),
(31, 'Peach and Banana Oat Smoothie', 1000, 'l', 'Vegan', 'https://www.eatthismuch.com/recipe/nutrition/peach-and-banana-oat-smoothie,1502784/'),
(32, 'Kale Avocado Salad', 1000, 'l', 'Vegan', 'https://www.eatthismuch.com/recipe/nutrition/kale-avocado-salad,906297/'),
(33, 'Vegetarian Fajita Pasta', 1000, 'd', 'Vegan', 'https://www.eatthismuch.com/recipe/nutrition/vegetarian-fajita-pasta,3251862/'),
(34, 'Chopped Radish and Avocado Salad', 1000, 'd', 'Vegan', 'https://www.eatthismuch.com/recipe/nutrition/chopped-radish-and-avocado-salad,907183/'),
(35, 'Mushroom and Soba Miso Soup', 1000, 'd', 'Vegan', 'https://www.eatthismuch.com/recipe/nutrition/mushroom-and-soba-miso-soup,963113/'),
(36, 'Simple Avocado and Cranberry Salad', 1000, 'd', 'Vegan', 'https://www.eatthismuch.com/recipe/nutrition/simple-avocado-and-cranberry-salad,905658/'),
-- ~2000
-- Balanced
(37, 'Turkey & Spinach Omelet', 2000, 'b', 'Balanced', 'https://www.eatthismuch.com/recipe/nutrition/tasty-turkey-spinach-omelet,56672/'),
(38, '2 Bananas', 2000, 'b', 'Balanced', 'https://www.eatthismuch.com/recipe/nutrition/banana,474253/'),
(39, 'Peach and Blueberry Parfait', 2000, 'b', 'Balanced', 'https://www.eatthismuch.com/recipe/nutrition/peach-and-blueberry-parfait,717844/'),
(40, 'Buttered Toast', 2000, 'b', 'Balanced', 'https://www.eatthismuch.com/recipe/nutrition/buttered-toast,254567/'),
(41, 'Peach and Bluebery Parfait', 2000, 'l', 'Balanced', 'https://www.eatthismuch.com/recipe/nutrition/peach-and-blueberry-parfait,717844/'),
(42, 'Strawberry and Walnut Spinach', 2000, 'l', 'Balanced', 'https://www.eatthismuch.com/recipe/nutrition/strawberry-and-walnut-spinach-salad,3266487/'),
(43, 'Quick Avocado Tuna Sandwich', 2000, 'l', 'Balanced', 'https://www.eatthismuch.com/recipe/nutrition/quick-avocado-tuna-sandwich,1012832/'),
(44, 'Brie and Celery', 2000, 'l', 'Balanced', 'https://www.eatthismuch.com/recipe/nutrition/brie-and-celery,906449/'),
(45, 'Cauliflower Fried Rice', 2000, 'd', 'Balanced', 'https://www.eatthismuch.com/recipe/nutrition/cauliflower-fried-rice,3237790/'),
(46, 'Tuna Apple Salad', 2000, 'd', 'Balanced', 'https://www.eatthismuch.com/recipe/nutrition/tuna-apple-salad,929984/'),
(47, 'Herb and Lemon Fish', 2000, 'd', 'Balanced', 'https://www.eatthismuch.com/recipe/nutrition/herb-and-lemon-fish,35073/'),
(48, 'Strawberry and Walnut Spinach Salad', 2000, 'd', 'Balanced', 'https://www.eatthismuch.com/recipe/nutrition/strawberry-and-walnut-spinach-salad,3266487/'),
-- Vegetarian
(49, 'High Protein Omelet', 2000, 'b', 'Vegetarian', 'https://www.eatthismuch.com/recipe/nutrition/high-protein-omelet,940672/'),
(50, 'Rice Cakes with Banana & Almond Butter', 2000, 'b', 'Vegetarian', 'https://www.eatthismuch.com/recipe/nutrition/rice-cakes-with-banana-almond-butter,332327/'),
(51, '3-Vegetable Tofu Scramble', 2000, 'b', 'Vegetarian', 'https://www.eatthismuch.com/recipe/nutrition/3-vegetable-tofu-scramble,3251633/'),
(52, 'Yogurt with Almonds & Honey', 2000, 'b', 'Vegetarian', 'https://www.eatthismuch.com/recipe/nutrition/yogurt-with-almonds-honey,3266363/'),
(53, 'Berry Granola Parfait', 2000, 'l', 'Vegetarian', 'https://www.eatthismuch.com/recipe/nutrition/berry-granola-parfait,33527/'),
(54, 'Cabbage Cucumber Salad', 2000, 'l', 'Vegetarian', 'https://www.eatthismuch.com/recipe/nutrition/cabbage-cucumber-salad,837533/'),
(55, 'Creamy Green Chia Smoothie', 2000, 'l', 'Vegetarian', 'https://www.eatthismuch.com/recipe/nutrition/creamy-green-chia-smoothie,927909/'),
(56, 'Simple Spinach Salad', 2000, 'l', 'Vegetarian', 'https://www.eatthismuch.com/recipe/nutrition/simple-spinach-salad,3087507/'),
(57, 'Quinoa Patties over Spinach', 2000, 'd', 'Vegetarian', 'https://www.eatthismuch.com/recipe/nutrition/quinoa-patties-over-spinach,208103/'),
(58, 'Bean Sprout and Spinach Salad', 2000, 'd', 'Vegetarian', 'https://www.eatthismuch.com/recipe/nutrition/bean-sprout-and-spinach-salad,3841269/'),
(59, 'Soba Noodles & Coconut Curry', 2000, 'd', 'Vegetarian', 'https://www.eatthismuch.com/recipe/nutrition/soba-noodles-coconut-curry,56737/'),
(60, 'Simple Mixed Greens Salad', 2000, 'd', 'Vegetarian', 'https://www.eatthismuch.com/recipe/nutrition/simple-mixed-greens-salad,948591/'),
-- Vegan
(61, 'Tofu Scrambled Eggs', 2000, 'b', 'Vegan', 'https://www.eatthismuch.com/recipe/nutrition/tofu-scrambled-eggs,717808/'),
(62, 'Strawberry Pear Juice', 2000, 'b', 'Vegan', 'https://www.eatthismuch.com/recipe/nutrition/strawberry-pear-juice,906491/'),
(63, 'Hummus Avocado Toast', 2000, 'b', 'Vegan', 'https://www.eatthismuch.com/recipe/nutrition/hummus-avocado-toast,1501613/'),
(64, 'Strawberry Pear Juice', 2000, 'b', 'Vegan', 'https://www.eatthismuch.com/recipe/nutrition/strawberry-pear-juice,906491/'),
(65, 'Vegan Chocolate Peanut Protein Shake', 2000, 'l', 'Vegan', 'https://www.eatthismuch.com/recipe/nutrition/vegan-chocolate-peanut-protein-shake,254482/'),
(66, 'Spinach Tomato Salad', 2000, 'l', 'Vegan', 'https://www.eatthismuch.com/recipe/nutrition/spinach-tomato-salad,3268333/'),
(67, 'Banana Blueberry Smoothie', 2000, 'l', 'Vegan', 'https://www.eatthismuch.com/recipe/nutrition/banana-blueberry-smoothie,412915/'),
(68, 'Red Bell Pepper and Hummus', 2000, 'l', 'Vegan', 'https://www.eatthismuch.com/recipe/nutrition/red-bell-pepper-and-hummus,3266266/'),
(69, 'Vegan Buffalo Chickpea Taquitos', 2000, 'd', 'Vegan', 'https://www.eatthismuch.com/recipe/nutrition/vegan-buffalo-chickpea-taquitos,374297/'),
(70, 'Green Pea & Almond Salad', 2000, 'd', 'Vegan', 'https://www.eatthismuch.com/recipe/nutrition/green-pea-almond-salad,225935/'),
(71, 'Spaghetti with Onion and Mushroom', 2000, 'd', 'Vegan', 'https://www.eatthismuch.com/recipe/nutrition/spaghetti-with-onion-and-mushroom,930887/'),
(72, 'Sautéed Kale', 2000, 'd', 'Vegan', 'https://www.eatthismuch.com/recipe/nutrition/sauteed-kale,906652/'),
-- >2200
-- Balanced
(73, 'Spicy Fried Eggs', 2300, 'b', 'Balanced', 'https://www.eatthismuch.com/recipe/nutrition/spicy-fried-eggs,34940/'),
(74, 'Cheese Tomato Bread', 2300, 'b', 'Balanced', 'https://www.eatthismuch.com/recipe/nutrition/goat-cheese-on-toasted-bread-with-tomato,905637/'),
(75, 'Orange Mango Smoothie', 2300, 'l', 'Balanced', 'https://www.eatthismuch.com/recipe/nutrition/orange-mango-smoothie-with-chia,951751/'),
(76, 'Green Bean Tuna Salad', 2300, 'l', 'Balanced', 'https://www.eatthismuch.com/recipe/nutrition/green-bean-healthy-tuna-salad,3268348/'),
(77, 'Turkey & Broccoli Rice', 2300, 'd', 'Balanced', 'https://www.eatthismuch.com/recipe/nutrition/basic-turkey-rice-and-broccolli,906894/'),
(78, 'Tomato and Radish Salad', 2300, 'd', 'Balanced', 'https://www.eatthismuch.com/recipe/nutrition/tomato-and-radish-salad,3268405/'),

(79, 'Pickle and Cheddar Sandwich', 2300, 'b', 'Vegetarian', 'https://www.eatthismuch.com/recipe/nutrition/pickle-and-cheddar-sandwich,3856392/'),
(80, 'Cinnamon Banana Mug Cake', 2300, 'b', 'Vegetarian', 'https://www.eatthismuch.com/recipe/nutrition/cinnamon-banana-mug-cake,906429/'),
(81, 'Mexican Cottage Cheese Salad', 2300, 'l', 'Vegetarian', 'https://www.eatthismuch.com/recipe/nutrition/mexican-cottage-cheese-salad,332547/'),
(82, 'Protein-boosted Yogurt', 2300, 'l', 'Vegetarian', 'https://www.eatthismuch.com/recipe/nutrition/protein-boosted-yogurt,3266381/'),
(83, 'Spaghetti with Mushrooms, Garlic and Oil', 2300, 'd', 'Vegetarian', 'https://www.eatthismuch.com/recipe/nutrition/spaghetti-with-mushrooms-garlic-and-oil,3837123/'),
(84, 'Thai Cucumber Salad', 2300, 'd', 'Vegetarian', 'https://www.eatthismuch.com/recipe/nutrition/thai-cucumber-salad,3268513/'),

(85, 'Scrambled Tofu on Toast', 2300, 'b', 'Vegan', 'https://www.eatthismuch.com/recipe/nutrition/scrambled-tofu-on-toast,1481928/'),
(86, 'Rice Cakes with Banana & Almond Butter', 2300, 'b', 'Vegan', 'https://www.eatthismuch.com/recipe/nutrition/rice-cakes-with-banana-almond-butter,332327/'),
(87, 'Smashed White Bean and Avocado Sandwich', 2300, 'l', 'Vegan', 'https://www.eatthismuch.com/recipe/nutrition/smashed-white-bean-and-avocado-sandwich,1497115/'),
(88, 'Strawberry, Peach, and Chia Smoothie', 2300, 'l', 'Vegan', 'https://www.eatthismuch.com/recipe/nutrition/strawberry-peach-and-chia-smoothie,906359/'),
(89, 'Rice and Beans', 2300, 'd', 'Vegan', 'https://www.eatthismuch.com/recipe/nutrition/rice-and-beans,3175976/'),
(90, 'Eggplants a la Dawlish', 2300, 'd', 'Vegan', 'https://www.eatthismuch.com/recipe/nutrition/eggplants-a-la-dawlish,3257821/');


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
INSERT INTO user_meals (uid, mid, complete, a_day) VALUES
(1, 2, 0, '2023-01-01'),
(1, 5, 1, '2023-01-01'),
(2, 3, 1, '2023-01-01'),
(3, 1, 1, '2023-01-01'),
(4, 4, 1, '2023-01-01'),
(5, 6, 0, '2023-01-01'),
(6, 7, 0, '2023-01-01'),
(7, 8, 1, '2023-01-01'),
(8, 4, 1, '2023-01-01'),
(1, 12, 1, '2023-01-01'),
(7, 13, 1, '2023-01-01'),
(3, 10, 0, '2023-01-01'),
(5, 4, 0, '2023-01-01'),
(1, 18, 0, '2023-01-01');

-- Insert data into user_workouts table
INSERT INTO user_workouts (uid, wid, complete, a_day) VALUES
(1, 2, 0, '2023-01-01'),
(2, 3, 0, '2023-01-01'),
(3, 1, 1, '2023-01-01'),
(4, 5, 0, '2023-01-01'),
(5, 4, 1, '2023-01-01'),
(6, 6, 0, '2023-01-01'),
(7, 8, 0, '2023-01-01'),
(8, 7, 1, '2023-01-01');

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
