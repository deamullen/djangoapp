

from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from django.views.generic import View
import json as simplejson
import urllib2 
from urllib2 import Request
import re

from .models import Choice, Question

def index(request):
    return render(request, 'andrea/index.html')

def contact(request):
    return render(request, 'andrea/contact.html')

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'andrea/detail.html', {
                      'question': question,
                      'error_message': "You didn't select a choice.",
                      })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('andrea:results', args=(question.id,)))

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'andrea/detail.html', {'question': question})

