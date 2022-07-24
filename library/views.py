from django.contrib import messages
from django.shortcuts import render,redirect,HttpResponse
from .models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .form import BookFrom


# Create your views here.

def index(request):
    return render(request, "index.html")

@login_required(login_url="/admin_login")
def add_book(request):
    if request.method == "POST":
        name = request.POST['name']
        author = request.POST['author']
        category = request.POST['category']
 
        books = Book.objects.create(name=name, author=author, category=category)
        books.save()
        alert = True
        return render(request, "add_book.html", {'alert':alert})
    return render(request, "add_book.html")


def view_books(request):
    books = Book.objects.all()
    return render(request, "view_books.html", {'books':books})


def delete_book(request, book_id):
    books = Book.objects.get(id=book_id)
    books.delete()
    return redirect("/view_books")

def edit_book(request, book_id):
    books = Book.objects.get(id=book_id)
    b=BookFrom(instance=books)
    if request.method == 'POST':
        b = BookFrom(request.POST,instance=books)
        b.is_valid()
        b.save()
        return redirect("/view_books")
    else:
        messages.error(request,b.errors)



    return render(request,"view_books.html",{'book':b})



def admin_login(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(email=email, password=password)

        if user is not None:
            login(request, user)
            if request.user.is_superuser:
                return redirect("/add_book")
            else:
                return HttpResponse("You are not an admin.")
        else:
            alert = True
            return render(request, "admin_login.html", {'alert':alert})
    return render(request, "admin_login.html")

def Logout(request):
    logout(request)
    return redirect ("/")


def student_registration(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password != confirm_password:
            passnotmatch = True
            return render(request, "student_registration.html", {'passnotmatch':passnotmatch})

        user = MyUser.objects.create_user(username=username, email=email, password=password )
        student = Student.objects.create(user=user)
        user.save()
        student.save()
        alert = True
        return render(request, "student_registration.html", {'alert':alert})
    return render(request, "student_registration.html")


def student_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            if request.user.is_superuser:
                return HttpResponse("You are not a student!!")
            else:
                return redirect("/view_books")
        else:
            alert = True
            return render(request, "student_login.html", {'alert':alert})
    return render(request, "student_login.html")


def admin_registration(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password != confirm_password:
            passnotmatch = True
            return render(request, "admin_registration.html", {'passnotmatch':passnotmatch})

        user = MyUser.objects.create_user(username=username, email=email, password=password,is_superuser=True )

        user.save()

        alert = True
        return render(request, "admin_registration.html", {'alert':alert})
    return render(request, "admin_registration.html")