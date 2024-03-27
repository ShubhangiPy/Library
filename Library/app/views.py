
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Book, Borrow
from datetime import datetime, timedelta

# Create your views here.

def home(request):
    books = Book.objects.all()
    return render(request, 'home.html', {'books': books})

@login_required
def borrow_book(request, book_id):
    book = Book.objects.get(id=book_id)
    if request.method == 'POST':
        if Borrow.objects.filter(borrower=request.user, returned=False).count() >= 10:
            return render(request, 'error.html', {'message': 'You have already borrowed the maximum number of books.'})
        if book.available_copies() > 0:
            return_date = datetime.now() + timedelta(days=30)
            borrow = Borrow.objects.create(book=book, borrower=request.user, return_date=return_date)
            borrow.save()
            return redirect('home')
        else:
            return_date = Borrow.objects.filter(book=book, returned=False).order_by('return_date').first().return_date
            return render(request, 'error.html', {'message': f'This book is not available. It will be returned by {return_date}.'})
    return render(request, 'library/borrow.html', {'book': book})

@login_required
def borrowed_books(request):
    borrowed_books = Borrow.objects.filter(borrower=request.user, returned=False)
    return render(request, 'borrowed_books.html', {'borrowed_books': borrowed_books})
