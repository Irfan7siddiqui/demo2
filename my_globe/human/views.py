from django.shortcuts import loader
from django.http import HttpResponse
from human.models import Number


def human(request):
  template = loader.get_template('first.html')
  
  vals = Number.objects.all().values()
  context = {"greet": "Hello",
             "users": vals}
  
  return HttpResponse(template.render(context, request))