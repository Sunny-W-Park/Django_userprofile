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

#Email authentification
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.core.mail import EmailMessage
from .tokens import account_activation_token
from django.utils.encoding import force_bytes, force_text


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
            user.is_active = False
            user.save()
            #Save in User Config
            #auth.login(request, user)
            signup = Signup(
                    name = form.data.get('name'),
                    email = form.data.get('username'),
                    nickname = form.data.get('nickname'),
                    )
            signup.save()
            #Save in Model
            current_site = get_current_site(request)
            #localhost:8000
            message = render_to_string(
                    'user_activate_email.html',
                    {'user': user,
                    'domain': current_site.domain,
                    'uid': urlsafe_base64_encode(force_bytes(user.pk)).encode().decode(),
                    'token': account_activation_token.make_token(user)
                    })
            #create token (tokens.py)
            mail_subject = '[Texter] 회원가입 인증 메일입니다.'
            user_email = user.username
            email = EmailMessage(mail_subject, message, to=[user_email])
            email.send()
            messages.info(request, '입력하신 이메일로 인증 링크가 전송되었습니다. 인증 후 로그인 가능합니다.')
            return redirect('signup')
            #TBC to redirect('daemun'), after adding message line into daemun.html
    context = {"form": form}
    return render(request, "signup.html", context)


def activate(request, uid64, token):
    uid = force_text(urlsafe_base64_decode(uid64))
    user = User.objects.get(pk=uid)
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        auth.login(request, user)
        return redirect('daemun')
    else:
        return HttpResponse('비정상적인 접근입니다.')

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
            if user.is_active:
                auth.login(request, user)
                return redirect('daemun')
            else:
                messages.info(request, '미인증 계정입니다. 이메일 인증을 완료해주세요.')
                return render(request, 'login.html', {'error': '미인증 계정'})
        else:
            messages.info(request, '아이디 혹은 비밀번호가 잘못 입력되었습니다.')
            return render(request, 'login.html', {'error': '아이디/비밀번호 오류'})
    else:
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('daemun')
