from django.urls import reverse
from django.db import models
import uuid

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


class BookInstance(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, help_text='書籍の一意のID')
    book = models.ForeignKey('Book', on_delete=models.SET_NULL, null=True)
    imprint = models.CharField(max_length=200)
    due_back = models.DateField(null=True, blank=True)

    LOAN_STATUS = (
        ('m', 'Maintenance'),
        ('o', 'On loan'),
        ('a', 'Available'),
        ('r', 'Reserved'),
    )

    status = models.CharField(
        max_length=1,
        choices=LOAN_STATUS,
        blank=True,
        default='m',
        help_text='書籍予約',
    )

    class Meta:
        ordering = ['due_back']

    def __str__(self):
        return f'{self.id} ({self.book.title})'


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField('Died', null=True, blank=True)

    class Meta:
        ordering = ['last_name', 'first_name']

    def get_absolute_url(self):
        return reverse('author-detail', args=[str(self.id)])

    def __str__(self):
        return f'{self.last_name}, {self.first_name}'
