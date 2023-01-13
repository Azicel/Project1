from django.contrib import admin

# Register your models here.

from .models import City_Sal, City_Count, Year


class CityAdminSal(admin.ModelAdmin):
    list_display = ['city_name_sal', 'city_sal']


class CityAdminCount(admin.ModelAdmin):
    list_display = ['city_name_count','city_count']


class YearAdmin(admin.ModelAdmin):
    list_display = ['year_date', 'year_sal_all', 'year_sal_job','year_count_all','year_count_job']


admin.site.register(City_Sal, CityAdminSal)
admin.site.register(Year, YearAdmin)
admin.site.register(City_Count, CityAdminCount)
