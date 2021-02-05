from django.urls import reverse
from django.db import models

# Create your models here.


class Genre(models.Model):
    name = models.CharField(max_length=200, help_text='本ジャンルを入力してください(SF,古典)')

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey("Author", on_delete=models.SET_NULL, null=True)
    summary = models.TextField(max_length=1000, help_text='ほんの簡単な説明を入力してください')
    isbn = models.CharField(
        "ISBN", max_length=13, help_text='13桁 <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>')
    genre = models.ManyToManyField(Genre, help_text='この本のジャンルを選択してください')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("book-detail", args={str(self.id)})
