import datetime

from django.db import models
from django.utils import timezone
from django.utils.encoding import python_2_unicode_compatible

# Create your models here.

@python_2_unicode_compatible
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

@python_2_unicode_compatible
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

@python_2_unicode_compatible
class Country(models.Model):
    country_name = models.CharField(max_length=200)
    favorite_local_food = models.CharField(max_length=200)
    favorite_tourist_spot = models.CharField(max_length=200)
    date_visited = models.DateField('date visited')

    def __str__(self):
        return self.country_name

@python_2_unicode_compatible
class City(models.Model):
    country_name = models.ForeignKey(Country, on_delete=models.CASCADE)
    city_name = models.CharField(max_length=200)
    length_of_stay = models.IntegerField(default=0)
    
    def __str__(self):
        return self.city_name
