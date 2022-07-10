from django.shortcuts import render
from django.http import HttpResponse
from .models import Widget
from django.views.generic.edit import CreateView
from .forms import AddWidgetForm

# Create your views here.
def home(request):
  widgets = Widget.objects.all()
  add_widget_form = AddWidgetForm()
  return render(request, 'index.html', {'widgets': widgets, 'add_widget_form': add_widget_form})

class widget_create(CreateView):
  model = Widget
  fields = '__all__'
  success_url = ''


