from django.shortcuts import render
from django.http import HttpResponse
from .models import*
# Create your views here.

def toLogin_view(request):
    return render(request, 'login.html')

def Login_view(request):
    username = request.POST.get("username",'')
    password = request.POST.get("password",'')

    if username and password:
        c=UserInfo.objects.filter(username = username, password=password).count()
        if c>=1:
            # return HttpResponse("To %s 登录成功！ Login successfully! "%username)
            return HttpResponse(content=
                "<a href=http://www.myreal.top/index_UCPPJIMcJMpYCgx9tKBvExlg.html>To %s Login successfully!</a>"%username,content_type='text/html')
        else:
            return HttpResponse("不正确的用户名或密码。Incorrect username or password!")
    else:
        return HttpResponse("请输入正确的用户名和密码。Please input username and password!")

# render register interface
def toregister_view(request):
    return render(request,'register.html')

def register_view(request):
    username = request.POST.get("username", '')
    password = request.POST.get("password", '')
    phone = request.POST.get("phone",'')
    email = request.POST.get("email",'')
    if username and password:
        c = UserInfo.objects.filter(username=username).count()
        if c >= 1:
            return HttpResponse("此用户名已存在注册失败。 Username already exist.")
        user = UserInfo(username=username,password=password,phone=phone,email=email)
        user.save()
        return HttpResponse("注册成功！ Register successfully!")
    else:
        return HttpResponse("请输入完整的用户名和密码。 Please input username and password.")

