<h1 style="text-align: center;"> Local Database Setup </h1>
<h3 style="text-align: center;"> Below are instrctions to setting up database locally </h3>

Database Setup
--------------
As of right now, there is currently no remote database host, so the database must be hosted locally for the time being.

1. Download PSQL and pgAdmin4
    - Download PSQL v15.5 from [this website](https://www.enterprisedb.com/downloads/postgres-postgresql-downloads) and choose your current OS to download the installer
    - Continue clicking next and once downloaded, pgAdmin4 will be installed alongside PSQL.
2. Using pgAdmin4
    - Once installed, open pgAdmin4 (*you may have to search for it using the Windows key or cmd+space to find the application*)
    - Once opened, you should see *PostgreSQL 15* as an available server under the server list on the left navbar.
        - It is worth noting that you may be asked to input a password. This password will be the **database password** and it is **imperative** that you don't forget it. 
    - Expand the *PostgreSQL 15* list bu clicking on the arrow and right click on Databases and create a new database
        - You **must** name this database **projhabits**
    - Once that is done, right click on *projhabits* on the left navbar and click on *Query Tool*. This tool will allow you to manually write SQL statements that will affect the database.
    - The query editor will appear on the right side of the screen. Here, you will first copy/paste the contents of [tables.sql](/backend/tables.sql) and copy/paste the contents of [populate.sql](/backend/populate.sql) and run the query using the play button above the editor. The *tables.sql* file creates the tables for the database and *populate.sql* populates the contents of each table in the database, hence, the contents of *tables.sql* must run first or before that of *populate.sql*.
3. Connect database server to Python server
    - In [main.py](/backend/main.py), modify the `DB_URL` variable where,
        - `db_pass` is the **database password**
        - `db_host` is the database host, which will be `localhost:[port ####]`
            - The port number can be found by right clicking *PostgreSQL* on the left navbar in pgAdmin4 > Properties > Connections in the *Port* field. The host can can also be found in the *Hostname/address* field.
    - Copy the modified URL and replace the URL in [env.py](/alembic/env.py) in line 13

Your local database should now be created and connected to the Python server.
