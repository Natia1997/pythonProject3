from django.forms import ModelForm
from .models import Room, Meal

class MealForm(ModelForm):
    class Meta:
        model = Meal
        fields = ['name', 'description','picture']