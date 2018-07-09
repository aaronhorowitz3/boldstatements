from django.shortcuts import render, redirect
from .models import Statement
from .forms import MakeAStatement
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseNotFound


# Create your views here.
def statement_feed(request):
    statements = Statement.objects.all()
    return render(request, 'boldstatements/statement_feed.html', {'statements': statements})

def statement_detail(request, pk):
    statement = Statement.objects.get(id=pk)
    return render(request, 'boldstatements/statement_detail.html', {'statement': statement})

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        raw_password = request.POST['password']
        user = authenticate(username=username, password=raw_password)
        login(request, user)
        return redirect('statement_feed')
    else:
        form = LoginForm()
    return render(request, 'boldstatements/login.html', {'form': form})

def signup_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('statement_feed')
    else:
        form = UserCreationForm()
    return render(request, 'boldstatements/signup.html', {'form': form})

@login_required
def make_a_statement(request):
    if request.method == 'POST':
        form = MakeAStatement(request.POST, request.FILES)
        if form.is_valid():
            statement = form.save()
            return redirect('statement_detail', pk=statement.pk)
    else:
        form = MakeAStatement()
    return render(request, 'boldstatements/new_statement.html', {'form': form})

def logout_user(request):
    logout(request)
    return redirect('statement_feed')
