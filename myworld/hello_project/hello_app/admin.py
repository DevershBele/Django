from django.contrib import admin
from .models import YourModel

admin.site.register(YourModel)


from .models import Author, Book

admin.site.register(Author)
admin.site.register(Book)