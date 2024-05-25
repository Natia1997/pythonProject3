from django.forms import ModelForm
from .models import Room

class MealForm(ModelForm):
    class Meta:
        model = Room
        fields = ['name', 'description']