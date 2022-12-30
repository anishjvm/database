from flask import Flask
from jproperties import Properties
import mysql.connector

configs = Properties()

with open('app-config.properties', 'rb') as config_file:
    configs.load(config_file)

host = configs.get("DB_HOST").data
database = configs.get("DB_SCHEMA").data
user = configs.get("DB_User").data
password = configs.get("DB_PWD").data
try:
    print("tesitng")
    connection = mysql.connector.connect(host=host,
                                         database=database,
                                         user=user,
                                         password=password)
    print("tesitng123")
except mysql.connector.Error as error:
        print("Failed to get record from MySQL table: {}".format(error))

from .models import *

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'Anish'

    from .views import views

    app.register_blueprint(views, url_prefix='/')

    return app
