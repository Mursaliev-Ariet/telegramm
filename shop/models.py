from django.db import models

class Clothes(models.Model):
    name = models.CharField(max_length=100)
    text = models.TextField()
    price = models.IntegerField()
    photo = models.ImageField(upload_to='clothes')
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Одежда'
        verbose_name_plural = 'Одежда'
