from django.db import models
from django.contrib import admin


class Extradition(models.Model):
    date_extradition = models.DateTimeField(auto_now_add=True, verbose_name="Дата выдачи")
    date_delivery = models.DateTimeField(verbose_name="Дата сдачи", blank=True,)
    id_library_card = models.ForeignKey(
        'Read_books',
        on_delete=models.CASCADE,
        related_name='id_library_card',
        verbose_name='Кому выдано',
        null=False,
        blank=True
    )


    class Meta:
        verbose_name = 'Выдачу книги'
        verbose_name_plural = 'Выдачи книги'


class Read_books(models.Model):
    id_read = M = models.BigIntegerField
    fn_read = models.CharField(max_length=15, verbose_name="Имя")
    ln_read = models.CharField(max_length=15, verbose_name="Фамилия")
    fatn_read = models.CharField(max_length=15, verbose_name="Отчество", null=True, blank=True, default='Нет отчества')
    birthday_read = models.DateField(verbose_name="Дата рождения", null=True)
    address_read = models.CharField(max_length=1500, verbose_name="Адрес читателя")
    contact_phone_read = models.CharField(max_length=20, verbose_name="Телефон читателя")

    def __str__(self):
        return self.ln_read + ' ' + self.fn_read + ' ' + self.fatn_read

    class Meta:
        verbose_name = 'Читателя'
        verbose_name_plural = 'Читатели'



