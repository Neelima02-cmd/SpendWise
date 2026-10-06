from django.contrib import admin
from django.urls import path
from expenses import views


urlpatterns = [
    path("admin/", admin.site.urls),

    path("", views.home, name="home"),

    path("login/", views.login_view, name="login"),

    path("register/", views.register, name="register"),

    path("logout/", views.logout_view, name="logout"),

    path(
        "delete/<int:expense_id>/",
        views.delete_expense,
        name="delete_expense"
    ),
]