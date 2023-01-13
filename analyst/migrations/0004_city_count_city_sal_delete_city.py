# Generated by Django 4.1.5 on 2023-01-11 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analyst', '0003_remove_city_city_name_city_city_name_count_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='City_Count',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city_name_count', models.CharField(default='Екатеринбург', max_length=30, verbose_name='Название города(доля)')),
                ('city_count', models.DecimalField(decimal_places=4, max_digits=5, verbose_name='Доля вакансий от общего числа')),
            ],
        ),
        migrations.CreateModel(
            name='City_Sal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city_name_sal', models.CharField(default='Екатеринбург', max_length=30, verbose_name='Название города(оклад)')),
                ('city_sal', models.BigIntegerField(verbose_name='Средний оклад в городе')),
            ],
        ),
        migrations.DeleteModel(
            name='City',
        ),
    ]