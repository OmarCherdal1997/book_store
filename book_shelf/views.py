from django.shortcuts import render
from . import models
# Create your views here.
def index (request):
    all_books = models.Book.objects.all()
    return render(request,"book_shelf/index.html",{
        "books": all_books
    })
