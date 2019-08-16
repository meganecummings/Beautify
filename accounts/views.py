from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.models import User

def sign_up(request):
  if request.method == "POST":
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    username = request.POST['username']
    email = request.POST['email']
    password = request.POST['password']
    password2 = request.POST['password2']

    if password == password2:
      if User.objects.filter(username=username).exists():
        return render(request, 'signup.html', {'error': 'That username already exists. Please choose a different username.'})
      else:
        if User.objects.filter(email=email).exists():
          return render(request, 'signup.html', {'error': 'That email already exists. Try logging in or use a different email'})
        else:
          user = User.objects.create_user(
            first_name=first_name, last_name=last_name, username=username, email=email, password=password)
          user.save()
          return redirect('login')
    else:
      return render(request, 'signup.html', {'error': 'Passwords do not match. Please try again.'})
  else:
    return render(request, 'signup.html')

def login(request):
  if request.method == "POST":
    username = request.POST.get('username')
    password = request.POST.get('password')

    user = auth.authenticate(username=username, password=password)

    if user is not None:
      auth.login(request, user)
      return redirect('home_view')
    else:
      return render(request, 'login.html', {'error': 'Invalid Credentials. Please try logging in again.'})
  else:
    return render(request, 'login.html')

def logout(request):
  auth.logout(request)
  return redirect('home_view')
