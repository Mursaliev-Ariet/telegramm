from django.db import models

class Clothes(models.Model):
    name = models.CharField(max_length=100, verbose_name="введите название одежды")
    text = models.TextField(verbose_name="описание. например размер, цвет и прочее")
    price = models.CharField(max_length=100, verbose_name="стоимость одежды")
    photo = models.ImageField(upload_to='clothes/', blank=True, null=True)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Одежда'
        verbose_name_plural = 'Одежда'
