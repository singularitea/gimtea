from django.contrib import admin
from .models import InstrumentType
from .models import InstrumentInformation
from .models import InstrumentReading

admin.site.register(InstrumentType)
admin.site.register(InstrumentInformation)
admin.site.register(InstrumentReading)
