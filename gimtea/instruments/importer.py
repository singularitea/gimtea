import csv
from .models import InstrumentReading

# Not working. Instrument ID is not recognised
def get_data(csv_file):
    dfile = open(csv_file, 'r')
    reader = csv.reader(dfile)
    rownum = 0
    for row in reader:
        if rownum == 0:
            rownum +=1
        else:
            the_row = InstrumentReading(instrument_id=row[0], read_date=row[1], reading=row[2])
            the_row.save()
