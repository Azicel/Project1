from django.shortcuts import render
from .models import City_Sal, City_Count, Year


# Create your views here.

def main(requset):
    return render(requset, 'analyst/main.html')


def years(requset):
    all_years_data = Year.objects.all()
    return render(requset, 'analyst/years.html',{'years_data':all_years_data})


def cities(request):
    all_cities_sal_data = City_Sal.objects.order_by('city_sal').reverse()
    all_cities_count_data = City_Count.objects.order_by('city_count').reverse()
    return render(request, 'analyst/cities.html', {'city_sal_data': all_cities_sal_data,
                                                   'city_count_data': all_cities_count_data,
                                                   })
