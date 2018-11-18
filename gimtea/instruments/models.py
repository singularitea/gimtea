from django.db import models

class InstrumentType(models.Model):
    instrument_type = models.CharField(max_length=70)
    def __str__(self):
        return str(self.instrument_type)

class InstrumentInformation(models.Model):
    class Meta:
        verbose_name_plural = 'Instrument information'
    instrument_name = models.CharField(max_length=70)
    instrument_type = models.ForeignKey(InstrumentType, on_delete=models.CASCADE)
    easting = models.DecimalField(max_digits=14, decimal_places=4)
    northing = models.DecimalField(max_digits=14, decimal_places=4)
    elevation = models.DecimalField(max_digits=10, decimal_places=4)
    def __str__(self):
        return str(self.instrument_name)

class InstrumentReading(models.Model):
    instrument_id = models.ForeignKey(InstrumentInformation, db_column='instrument_name', on_delete=models.CASCADE)
    read_date = models.DateTimeField()
    reading = models.DecimalField(max_digits=14, decimal_places=4)
    def __str__(self):
        return "{} - {} - {}".format(self.instrument_id,self.read_date,self.reading)
        #return str(self.instrument_id)
