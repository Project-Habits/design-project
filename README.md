<h1 style="text-align: center;"> Project Habits </h1>
<h2 style="text-align: center;"> CS 3493 Design Project </h2>
<h6 style="text-align: center;"> William Liburd, Justin Cheok, Amy Bobb, Dylan Imperato, Anson Zou </h6>

## Database Setup

The application currently uses CockroachDB Serverless to host the database on a cloud server. For information on how to setup the database _locally_, refer to the [README](backend/README.md) in the backend directory.

1. Install CockroachDB support for SqlAlchemy
   - `pip install sqlalchemy-cockroachdb`
2. Run command on terminal
   - If on Windows:
     - `mkdir -p $env:appdata\postgresql\; Invoke-WebRequest -Uri https://cockroachlabs.cloud/clusters/407eeef5-0a45-444f-b7bd-206f992d9952/cert -OutFile $env:appdata\postgresql\root.crt`
   - If on MacOS:
     - `curl --create-dirs -o $HOME/.postgresql/root.crt 'https://cockroachlabs.cloud/clusters/407eeef5-0a45-444f-b7bd-206f992d9952/cert'`
3. An invite to the dashboard for the database cluster has been sent to your email.
   - If you don't have a CockroachDB account, make sure to register for one.
   - If you haven't received the invite, ping the backend team on _#backend_ or email wl2352@nyu.edu

The remote database should now be connected to the Python server.

## Starting Python App

1. Installing Python Packages with pip
   In order to start the Python server, one will have to install all of the associated packages within [main.py](backend/main.py):

- fastapi
- python-jose
- pydantic
- sqlalchemy
- sqlalchemy_cockroachdb
- uvicorn
- passlib
- fastapi_sqlalchemy
- bcrypt
- psycopg2

  This can be done with: `pip install fastapi python-jose pydantic sqlalchemy sqlalchemy_cockroachdb uvicorn passlib fastapi_sqlalchemy bcrypt psycopg2`

2. Starting the Python server
   Navigate to the [backend directory](backend/) and enter `python3 -m uvicorn main:app` into the console. This will initiate the Python server, enabling the proper functioning of the web app.

## Starting Web App

The web app must be started using a local server. Opening it locally _will not work_.

If you have access to VSCode, the plugin [Live Server](https://marketplace.visualstudio.com/items?itemName=ritwickdey.LiveServer) works. Follow the instructions in the plugin page to start the live server, ensuring that the project folder is open. Alternatively, you can open [index.html](index.html), right click, and click `Open with Live Server` after installing the plugin.

If you prefer to use the terminal to start the web app, a plugin that works is [live-server](https://www.npmjs.com/package/live-server), and this requires node.js and npm. By navigating to the base directory, you can then issue the command `live-server` which will automatically launch the default browser with the web app.
