from django.contrib import admin
from app.models import Book, Borrow

# Register your models here.
admin.site.register(Book)
admin.site.register(Borrow)