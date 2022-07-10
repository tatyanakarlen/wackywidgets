from django.forms import ModelForm
from .models import Widget

class AddWidgetForm(ModelForm):
    class Meta:
        model = Widget
        fields = ['description', 'quantity']