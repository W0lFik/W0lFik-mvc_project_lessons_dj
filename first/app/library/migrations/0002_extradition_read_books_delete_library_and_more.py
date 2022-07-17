# Generated by Django 4.0.5 on 2022-06-26 06:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Extradition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_extradition', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Дата выдачи')),
                ('date_delivery', models.DateTimeField(blank=True, null=True, verbose_name='Дата выдачи')),
            ],
            options={
                'verbose_name': 'Выдача',
                'verbose_name_plural': 'Выдачи',
            },
        ),
        migrations.CreateModel(
            name='Read_books',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fn_read', models.CharField(max_length=15, verbose_name='Имя')),
                ('ln_read', models.CharField(max_length=15, verbose_name='Фамилия')),
                ('fatn_read', models.CharField(blank=True, max_length=15, null=True, verbose_name='Отчество')),
                ('address_read', models.CharField(max_length=1500, verbose_name='Адрес читателя')),
                ('contact_phone_read', models.CharField(max_length=20, verbose_name='Номер телефона читателя')),
            ],
            options={
                'verbose_name': 'Читатель',
                'verbose_name_plural': 'Читатели',
            },
        ),
        migrations.DeleteModel(
            name='Library',
        ),
        migrations.AddField(
            model_name='extradition',
            name='id_library_card',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='book_name', to='library.read_books', verbose_name='ID книги'),
        ),
    ]