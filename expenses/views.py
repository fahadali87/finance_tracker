from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import Expense

import matplotlib
matplotlib.use('Agg')  # Required for server-side rendering

import matplotlib.pyplot as plt
import io
import base64
from django.db.models import Sum


@login_required
def dashboard(request):
    expenses = Expense.objects.filter(user=request.user)

    # Aggregate expenses by category
    category_data = (
        expenses
        .values('category')
        .annotate(total=Sum('amount'))
    )

    categories = [item['category'] for item in category_data]
    totals = [float(item['total']) for item in category_data]

    # Generate Pie Chart using Matplotlib
    chart = None
    if categories and totals:
        plt.figure(figsize=(6,6))
        plt.pie(totals, labels=categories, autopct='%1.1f%%')
        plt.title('Expense Distribution by Category')

        buffer = io.BytesIO()
        plt.savefig(buffer, format='png')
        buffer.seek(0)
        image_png = buffer.getvalue()
        buffer.close()
        plt.close()

        chart = base64.b64encode(image_png).decode('utf-8')

    context = {
        'expenses': expenses,
        'chart': chart
    }

    return render(request, 'dashboard.html', context)


@login_required
def add_expense(request):
    if request.method == 'POST':
        date = request.POST.get('date')
        amount = request.POST.get('amount')
        category = request.POST.get('category')
        description = request.POST.get('description')

        Expense.objects.create(
            user=request.user,
            date=date,
            amount=amount,
            category=category,
            description=description
        )

        return redirect('dashboard')

    return render(request, 'add_expense.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()

    return render(request, 'register.html', {'form': form})