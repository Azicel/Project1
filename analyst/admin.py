from django.contrib import admin

# Register your models here.

from .models import City, Year


class CityAdmin(admin.ModelAdmin):
    list_display = ['city_name', 'city_sal', 'city_count']


class YearAdmin(admin.ModelAdmin):
    list_display = ['year_date', 'year_sal_all', 'year_sal_job','year_count_all','year_count_job']


admin.site.register(City, CityAdmin)
admin.site.register(Year, YearAdmin)
