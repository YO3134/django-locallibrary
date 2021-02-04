from django.db import models

# Create your models here.


class Genre(models.Model):
    name = models.CharField(max_length=200, help_text='本ジャンルを入力してください(SF,古典)')

    def __str__(self):
        return self.name
