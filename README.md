# SweTaxCal
An application that automatically calculates swedish per diems.


## Working in a virtual environment:

1. Open the command line and navigate to the directory where you want to create the virtual environment.

2. Run the command `python -m venv venv` (python3) to create the virtual environment.

3. Activate the virtual environment by running the command windows:`venv\Scripts\activate.ps1` or mac:`source venv/bin/activate`

4. Deactivate

## How to use env variables:

1. from dotenv import load_dotenv
2. load_dotenv()
3. create .env file
4. os.getenv()

# .env file layout:
DATABASE_URL=mongodb+srv://<username>:<password>@<cluster>.cxedcay.mongodb.net/<collection>?retryWrites=true&w=majority
MONGO_USER=
MONGO_USER_PWD=

DATABASE_FULL=mongodb+srv://<username>:<password>@<cluster>.cxedcay.mongodb.net/<collection>?retryWrites=true&w=majority

SECRET_KEY=

## make a requirements file:

(Not used for the moment)
pip freeze > requirements.txt

## To install modules:

pip install -r requirements.txt

## Modules to be used:

- Flask
- Flask-PyMongo
- Flask-Login
- python-dotenv

## Project Structure:

to be updated

Using mongoDB on pythonanywhere:
https://help.pythonanywhere.com/pages/MongoDB/

https://flask-pymongo.readthedocs.io/en/latest/

Local mongodb database:

- brew services start mongodb-community@6.0
- brew services stop mongodb-community@6.0
