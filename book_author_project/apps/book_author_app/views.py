from django.shortcuts import render, redirect
from .models import Book,Author

def index(request):
    return render(request,"book_author_app/index.html")

def books(request):
    context = {
        "all_books" : Book.objects.all()
    }
    return render(request,"book_author_app/books.html", context)
def authors(request):
    context={
        "all_authors" : Author.objects.all()
    }
    return render(request,"book_author_app/authors.html", context)

def add_book(request):
    new_book = Book.objects.create(title=request.POST['book_title'], description=request.POST['book_disc'])
    return redirect ("/books")
def add_author(request):
    new_author = Author.objects.create(name=request.POST['a_name'], notes=request.POST['notes'])
    return redirect("/authors")

def book_descrip(request, book_id):
    context={
        "book_decription" : Book.objects.get(id=book_id),
        "book_authors" : Book.objects.get(id=book_id).authors.all(),
        "all_authors" : Author.objects.all(),
        #"book_not_authors" : Author.objects.exlude(books = book_id),
    }
    return render(request, "book_author_app/book_desc.html", context)

def author_descrp(request,author_id):
    context={
        "author_information" : Author.objects.get(id=author_id),
        "all_books" : Book.objects.all(),
        "author_book" : Author.objects.get(id=author_id).books.all(),
    }
    return render(request, "book_author_app/author_desc.html", context)
def add_author_to_book(request, book_id):
    book = Book.objects.get(id = book_id)
    author = Author.objects.get(id = request.POST["add_author_to_book"])
    book.authors.add(author)
    #add_relationship = Book.objects.get(id=book_id).authors.add(Author.objects.get(id=request.POST["add_author_to book"]))
    return redirect(f"/books/{book_id}")

def add_book_to_author(request, author_id):
    author = Author.objects.get(id= author_id)
    book1 = Book.objects.get(id=request.POST["select_book_to_add"])
    author.books.add(book1)
    return redirect(f"/authors/{author_id}")