import RPi.GPIO as GPIO
from time import sleep
from datetime import datetime
import mariadb
from cred import *


def getutc():
    return datetime.utcnow()

def write_soilmoisture(table) -> None:
    """Executes SQL statements
    :param table, con:
    :return:
    """
    connection = mariadb.connect(
        host=db_host, user=db_user, password=db_pass, database=db_name
    )
    statement = f"INSERT INTO {table} (time, state) VALUES('{getutc()}', '{get_moisture()}');"

    cursor = connection.cursor()
    cursor.execute(statement)
    connection.commit()
    return None

def get_moisture():

    GPIO.setmode(GPIO.BCM)

    inputpin = 4

    GPIO.setup(inputpin, GPIO.IN)
    state = GPIO.input(inputpin)

    print(state)

    if state == 1:
        return "feucht"
    else:
        return "trocken"

write_soilmoisture("soil")

GPIO.cleanup()