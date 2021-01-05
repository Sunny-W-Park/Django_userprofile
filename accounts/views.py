from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import auth

from django.shortcuts import render, redirect

#Pop-up message
from django.contrib import messages

#Import model
from .models import Signup

#Signup form
from .forms import SignupForm
from accounts.forms import SignupForm


def daemun(request):
    return render(request, 'daemun.html')

#Signup form
def signupform(request):
    form = SignupForm()

    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                    username = request.POST["username"],
                    password = request.POST["password1"],
                    )
            #Save in User Config
            auth.login(request, user)
            signup = Signup(
                    name = form.data.get('name'),
                    email = form.data.get('username'),
                    nickname = form.data.get('nickname'),
                    )
            signup.save()
            messages.info(request, '환영합니다.')
            return redirect('signup')
            #TBC to redirect('daemun'), after adding message line into daemun.html
    context = {"form": form}
    return render(request, "signup.html", context)


#def signup(request):
#    if request.method == "POST":
#        if request.POST["password1"] == request.POST["password2"]:
#            user = User.objects.create_user(
#                    username = request.POST["username"],
#                    password = request.POST["password1"]
#                    )
#            auth.login(request, user)
#            return redirect('daemun')
#        return render(request, 'signup.html')
#
#    return render(request, 'signup.html')

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username = username, password = password)
        if user is not None:
            auth.login(request, user)
            return redirect('daemun')
        else:
            return render(request, 'login.html', {'error': '아이디 혹은 비밀번호가 잘못 입력되었습니다.'})
    else:
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('daemun')
