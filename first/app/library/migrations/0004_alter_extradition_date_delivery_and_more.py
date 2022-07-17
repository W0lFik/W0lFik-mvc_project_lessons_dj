# Generated by Django 4.0.5 on 2022-06-26 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0003_alter_read_books_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='extradition',
            name='date_delivery',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='Дата получение'),
        ),
        migrations.AlterField(
            model_name='extradition',
            name='date_extradition',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='Дата выдачи'),
        ),
    ]
