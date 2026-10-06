from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User

from .models import Expense, Budget


@login_required(login_url="/login/")
def home(request):

    budget_object, created = Budget.objects.get_or_create(
        user=request.user,
        defaults={"amount": 10000}
    )

    if request.method == "POST":

        form_type = request.POST.get("form_type")

        # SAVE CUSTOM BUDGET
        if form_type == "budget":

            budget_amount = request.POST.get("budget_amount")

            if budget_amount:

                budget_object.amount = budget_amount
                budget_object.save()

            return redirect("home")

        # ADD EXPENSE
        if form_type == "expense":

            name = request.POST.get("expense_name")
            amount = request.POST.get("expense_amount")
            category = request.POST.get("expense_category")

            if name and amount:

                Expense.objects.create(
                    user=request.user,
                    name=name,
                    amount=amount,
                    category=category or "Other"
                )

            return redirect("home")

    expenses = Expense.objects.filter(
        user=request.user
    ).order_by("-date")

    total = sum(
        expense.amount
        for expense in expenses
    )

    budget = budget_object.amount

    remaining = budget - total

    percentage = 0

    if budget > 0:
        percentage = float((total / budget) * 100)

    # BUDGET STATUS

    if percentage >= 100:

        alert_message = (
            "🔴 Oh no! You've gone over your budget. "
            "Time to slow down the spending a little."
        )

        alert_class = "danger"

        status_text = "Over Budget"

    elif percentage >= 80:

        alert_message = (
            "🟠 You're getting close to your budget limit. "
            "Keep an eye on your spending!"
        )

        alert_class = "warning"

        status_text = "Near Budget"

    else:

        alert_message = (
            "🟢 You're doing great! "
            "You're safely within your budget."
        )

        alert_class = "success"

        status_text = "Safe"

    context = {
        "expenses": expenses,
        "total": total,
        "budget": budget,
        "remaining": remaining,
        "percentage": percentage,
        "alert_message": alert_message,
        "alert_class": alert_class,
        "status_text": status_text,
        "categories": Expense.CATEGORY_CHOICES,
    }

    return render(
        request,
        "expenses/index.html",
        context
    )


@login_required(login_url="/login/")
def delete_expense(request, expense_id):

    if request.method == "POST":

        expense = get_object_or_404(
            Expense,
            id=expense_id,
            user=request.user
        )

        expense.delete()

    return redirect("home")


def register(request):

    if request.method == "POST":

        username = request.POST.get("username")
        password = request.POST.get("password")

        if username and password:

            if not User.objects.filter(
                username=username
            ).exists():

                user = User.objects.create_user(
                    username=username,
                    password=password
                )

                login(request, user)

                return redirect("home")

    return render(
        request,
        "expenses/register.html"
    )


def login_view(request):

    if request.method == "POST":

        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:

            login(request, user)

            return redirect("home")

    return render(
        request,
        "expenses/login.html"
    )


def logout_view(request):

    if request.method == "POST":

        logout(request)

    return redirect("login")