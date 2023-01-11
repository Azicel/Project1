from django.db import models

# Create your models here.


class Vacancy(models.Model):
    vacancy_name = models.CharField('Название вакансии', max_length=50)
    vacancy_skills = models.TextField('Навыки')
    vacancy_salary_from = models.IntegerField('Нижняя вилка оклада')
    vacancy_salary_to = models.IntegerField('Верхняя вилка оклада')
    vacancy_salary_currency = models.CharField('Валюта', max_length= 3)
    vacancy_area = models.CharField('Город', max_length=30)
    vacancy_date = models.DateTimeField('Дата публикации')


class Year(models.Model):
    year_date = models.IntegerField('Год')
    year_sal_all = models.BigIntegerField('Средний оклад в год')
    year_sal_job = models.BigIntegerField('Средний оклад в год для профессии')
    year_count_all = models.IntegerField('Кол-во вакансий')
    year_count_job = models.IntegerField('Кол-во вакансий для профессии')


class City(models.Model):
    city_name = models.CharField('Название города', max_length= 30)
    city_sal = models.BigIntegerField('Средний оклад в городе')
    city_count = models.DecimalField('Доля вакансий от общего числа', max_digits=5, decimal_places=4)