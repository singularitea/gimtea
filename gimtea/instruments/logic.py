from .models import InstrumentReading

class newObject():
    def __init__(self, reading):
        self.reading = reading


def readings(data):
    reading_data = []
    print(data)
    for row in data:
        reading_data.append((row.read_date, row.reading))
        #print(reading_data[0])
    return reading_data
