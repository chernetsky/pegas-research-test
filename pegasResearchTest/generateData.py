from datetime import datetime, timedelta
from random import randint
import json


def randomIntGenerator(minValue=0, maxValue=100, maxIterations=10000):
    counter = 0
    while counter < maxIterations:
        counter += 1
        yield randint(minValue, maxValue)


def datetimeGenerator(start, end, delta=timedelta(minutes=5)):
    current = start
    while current < end:
        current += delta
        yield current
        

intVal = randomIntGenerator()

data = [{'timestamp': dt.timestamp(), 'value': next(intVal)} for dt in datetimeGenerator(datetime(2020, 1, 1), datetime(2020, 1, 1, 12))]

# print(data)

with open('data.json', 'w') as outfile:
    json.dump(data, outfile)
