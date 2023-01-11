from django import forms
from .models import City, Year


class CityForm(forms.ModelForm):
    class Meta:
        model = City
        fields = '__all__'


class YearForm(forms.ModelForm):
    class Meta:
        model = Year
        fields = '__all__'
