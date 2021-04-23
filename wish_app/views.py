from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
import bcrypt


def index(request):
    return render(request, "index.html")


def register(request):
    errors = User.objects.basic_validator(request.POST)
    if errors:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')

    password = request.POST['password']
    pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
    print(pw_hash)

    this_user = User.objects.create(
        first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'], password=pw_hash)
    request.session['user_id'] = this_user.id

    return redirect('/')


def login(request):
    user = User.objects.filter(email=request.POST['email'])
    if User:
        logged_user = user[0]
        if bcrypt.checkpw(request.POST['password'].encode(), logged_user.password.encode()):
            request.session['user_id'] = logged_user.id
            return redirect('/main')
    messages.error(request, "Invalid login")
    return redirect('/')


def main(request):
    user_id = request.session['user_id']
    context = {
    "this_user": User.objects.get(id=user_id),
    "wish": User.objects.all()
    }
    return render(request, "main.html", context)


def logout(request):
    if "user_id" not in request.session:
        return redirect('/')
    del request.session['user_id']
    return redirect("/")


def view_stats(request):
    return redirect('/main')


def make_a_wish(request):
        user_id = request.session['user_id']
        context = {
        "this_user": User.objects.get(id=user_id)
        }
        return render(request, 'make_a_wish.html')


def wish_list(request):
    user_id = request.session['user_id']
    context = {
        "user": User.objects.get(id=user_id).__dict__
    }
    return render(request, 'main.html', context)


def remove(request):
    return render(request, 'main.html')


def edit(request):
    user_id = request.session['user_id']
    context = {
        "this_user": User.objects.get(id=user_id)
    }
    return render(request, 'edit.html', context)


def granted_wishes(request):
    return render(request, 'main.html')


def like(request):
    return render(request, "/main")


def cancel(request):
    return render(request, "main.html")


def submit(request):
    user_id = request.session['user_id']
    User.objects.create(wish=request.POST["wish"], description=request.POST["description"])
    return redirect('/main')
