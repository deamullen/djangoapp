from django.contrib import admin

# Register your models here.
from .models import Question
from .models import City
from .models import Country

admin.site.register(Question)
admin.site.register(Country)
admin.site.register(City)

