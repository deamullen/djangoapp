

from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from django.views.generic import View
import json as simplejson
import urllib2 
from urllib2 import Request

from .models import Choice, Question

def index(request):
    return render(request, 'polls/index.html')


def world(request):
    return render(request, 'polls/around-the-world.html', {'weather_list' : get_weather_list()})


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
                      'question': question,
                      'error_message': "You didn't select a choice.",
                      })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})

def get_weather_list():
    weather_list = []
    search_url = 'https://query.yahooapis.com/v1/public/yql?q=select%20item.condition%2C%20location%20from%20weather.forecast%20where%20woeid%20in%20(select%20woeid%20from%20geo.places(1)%20where%20text%3D%22honolulu%2C%20hi%22)&format=json&env=store%3A%2F%2Fdatatables.org%2Falltableswithkeys'
    req = Request(search_url)
    raw = urllib2.urlopen(req)
    js = raw.readlines()
    js_object = simplejson.loads(js[0])

    item = js_object['query']['results']['channel']
    city = item['location']['city']
    item = js_object['query']['results']['channel']['item']['condition']
    date = item['date']
    temp = item['temp']
    condition = item['text']
    thisweather = weather(city, temp, condition, date)

    weather_list.append(thisweather)

    search_url = 'https://query.yahooapis.com/v1/public/yql?q=select%20item.condition%2C%20location%20from%20weather.forecast%20where%20woeid%20in%20(select%20woeid%20from%20geo.places(1)%20where%20text%3D%22sao%20paulo%22)&format=json&env=store%3A%2F%2Fdatatables.org%2Falltableswithkeys'
    req = Request(search_url)
    raw = urllib2.urlopen(req)
    js = raw.readlines()
    js_object = simplejson.loads(js[0])

    item = js_object['query']['results']['channel']
    city = item['location']['city']
    item = js_object['query']['results']['channel']['item']['condition']
    date = item['date']
    temp = item['temp']
    condition = item['text']
    thisweather = weather(city, temp, condition, date)

    weather_list.append(thisweather)

    search_url = 'https://query.yahooapis.com/v1/public/yql?q=select%20item.condition%2C%20location%20from%20weather.forecast%20where%20woeid%20in%20(select%20woeid%20from%20geo.places(1)%20where%20text%3D%22london%22)&format=json&env=store%3A%2F%2Fdatatables.org%2Falltableswithkeys'
    req = Request(search_url)
    raw = urllib2.urlopen(req)
    js = raw.readlines()
    js_object = simplejson.loads(js[0])

    item = js_object['query']['results']['channel']
    city = item['location']['city']
    item = js_object['query']['results']['channel']['item']['condition']
    date = item['date']
    temp = item['temp']
    condition = item['text']
    thisweather = weather(city, temp, condition, date)

    weather_list.append(thisweather)

    return weather_list

class weather(object):
    def __init__(self, city, temp, condition, date):
        self.city = city
        self.temp = temp
        self.condition = condition
        self.date = date
