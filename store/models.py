from distutils.command.upload import upload
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    slug = models.SlugField(max_length=150, unique=True, db_index=True)
    parent = models.ForeignKey(
        "self", on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name


class Publisher(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=150, unique=True, db_index=True)
    description = models.TextField()

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=150, unique=True, db_index=True)
    description = models.TextField()
    avatar = models.FileField(upload_to='author_pic/')
    create_at = models.DateTimeField(auto_now=True)
    update_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Book(models.Model):
    name = models.CharField(max_length=100)
    slug = models.CharField(max_length=100, db_index=True, unique=True)
    price = models.DecimalField(max_digits=8, decimal_places=3,
                                validators=[
                                    MaxValueValidator(99999),
                                    MinValueValidator(0)
                                ],
                                default=0)
    quantity = models.IntegerField()
    coverpage = models.FileField(upload_to="coverpage/")
    bookpage = models.FileField(upload_to="bookpage/")
    description = models.TextField()
    total_review = models.IntegerField(default=1)
    rating = models.IntegerField(default=0)
    state = models.IntegerField(default=0)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    sold_quantity = models.IntegerField(default=0)
    ISBN = models.CharField(max_length=100)
    public_year = models.DateField()
    language = models.CharField(max_length=20)
    weight = models.DecimalField(max_digits=4,
                                 decimal_places=2)
    size = models.CharField(max_length=100)
    form_id = models.IntegerField(default=0)
    discount = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Review(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    review_star = models.IntegerField()
    content = models.TextField()
    image_link = models.CharField(max_length=255)
    create_at = models.DateTimeField(auto_now=True)


class BookCategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
