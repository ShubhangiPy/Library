from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=100)
    copies = models.IntegerField(default=1)

    def available_copies(self):
        return self.copies - self.borrow_set.filter(returned=False).count()

class Borrow(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    borrower = models.ForeignKey(User, on_delete=models.CASCADE)
    borrowed_date = models.DateField(auto_now_add=True)
    return_date = models.DateField(auto_now_add=False)
    renewed = models.BooleanField(default=False)
    returned = models.BooleanField(default=False)
