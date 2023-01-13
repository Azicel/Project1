from django import forms
from .models import City_Sal, City_Count, Year


class CityFormSal(forms.ModelForm):
    class Meta:
        model = City_Sal
        fields = '__all__'


class CityFormCount(forms.ModelForm):
    class Meta:
        model = City_Count
        fields = '__all__'


class YearForm(forms.ModelForm):
    class Meta:
        model = Year
        fields = '__all__'
