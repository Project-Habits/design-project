<h1 style="text-align: center;"> Project Habits </h1>
<h2 style="text-align: center;"> CS 3493 Design Project </h2>
<h6 style="text-align: center;"> William Liburd, Justin Cheok, Amy Bobb, Dylan Imperato, Anson Zou </h6>

__TODO__
---------
- Complete the meals spreadsheet
- Encode passwords and other data
- Privatize database credentials
- Finish suggestions algorithm
- Outsource database hosting (**Must be a host that supports SQL**)
- Improve README and other documentation
    - Provide documentation for dev setup
        - Database
        - Website server
        - Python server

Database Setup
--------------
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
    - If you haven't received the invite, ping the backend team on *#backend* or email wl2352@nyu.edu

The remote database should now be connected to the Python server.
