from django.urls import path
from library import views

urlpatterns = [
    path("", views.index, name="index"),
    path("add_book/", views.add_book, name="add_book"),
    path("view_books/", views.view_books, name="view_books"),

    path("edit_book/<int:book_id>/", views.edit_book, name="edit_book"),
    path("delete_book/<int:book_id>/", views.delete_book, name="delete_book"),

    #admin
    path("admin_registration/", views.admin_registration, name="admin_registration"),
    path("admin_login/", views.admin_login, name="admin_login"),
    path("logout/", views.Logout, name="logout"),

    #student
    path("student_registration/", views.student_registration, name="student_registration"),
    path("student_login/", views.student_login, name="student_login"),
 

]