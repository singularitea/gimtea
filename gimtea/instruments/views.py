from django.shortcuts import render
from .importer import get_data
from .models import InstrumentReading
from .logic import readings

# Create your views here.
def importer(request):
    get_data('/home/ben/Dropbox/Programming/Projects/gimtea/gimtea/instruments/data.csv')
    return render(request, 'test.html')

def chart(request):
    data = InstrumentReading.objects.all()
    return_data = readings(data)
    return render(request, 'test.html', {'webdata': return_data})
