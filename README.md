**RUN MIGRATION DB**

You can run the database migration using the following commands:

`python3 manage.py db init`

`python3 manage.py db migrate`

`python3 manage.py db upgrade`

or run the script: `.run-migrations.sh`

**RUN APPLICATION**

To run the application:

`export FLASK_APP=main.py$FLASK_APP`

`flask run`

**TEST APPLICATION**

Request: `http://localhost:5000/pets`

Method: POST

Body: 

`
{
    "pet_name": "Bianca",
    "age": "1",
    "gender": "F"
}
`

**CONTAINER**

Please run the following command:

`docker-compose up -d`

If you do a change over the application please run:

`docker-compose up -d --no-deps --build api`



