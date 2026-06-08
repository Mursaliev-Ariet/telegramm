from django.db import models

class Clothes(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name="введите название одежды"
    )

    text = models.TextField(
        verbose_name="описание. например размер, цвет и прочее"
    )

    price = models.CharField(
        max_length=100,
        verbose_name="стоимость одежды"
    )

    image = models.ImageField(
        upload_to="images/",
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Одежда'
        verbose_name_plural = 'Одежда'

class Officiant(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "Официант"
        verbose_name_plural = "Официанты"

class Flower(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "Цветы"
        verbose_name_plural = "Цветы"