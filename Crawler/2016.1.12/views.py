# coding:utf-8
from django.shortcuts import render_to_response
from gushi.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django import forms
# 提交表单必须导入这个模块，因为request默认是Content模块，但是表单要使用RequestContext
from django.template import RequestContext
from django.core.exceptions import ObjectDoesNotExist


#  注册
# 定义表单类型
class UserRegisterForm(forms.Form):
    username = forms.CharField(label='用户名', max_length=100)
    password = forms.CharField(label='密码', widget=forms.PasswordInput())
    email = forms.EmailField(label='电子邮件')


# register
# 视图函数中给render_to_response增加一个参数:context_instance=RequestContext(request)  ？？为啥？
def register(request):
    if request.method == 'POST':
        uf = UserRegisterForm(request.POST)
        if uf.is_valid():
            # 获取表单信息
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']
            email = uf.cleaned_data['email']
            # 将表单写入数据库
            try:
                username = User.objects.get(username=username)
                print("这个用户已经存在需要再写一个html")
            except:
                user = User()
                user.username = username
                user.password = password
                user.email = email
                user.user_id = 0
                user.save()
                return HttpResponseRedirect('/login/')
    else:
        uf = UserRegisterForm()
        return render_to_response('register.html', {'uf': uf})


# 登录
# 定义表单类型
class UserLoginForm(forms.Form):
    username = forms.CharField(label='用户名', max_length=100)
    password = forms.CharField(label='密码', widget=forms.PasswordInput())


# 登录login
def login(request):
    if request.method == 'POST':
        print("post")
        uf = UserLoginForm(request.POST)
        if uf.is_valid():
            # 获取表单信息
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']
            # 获得的表单和数据库比较
            try:
                user = User.objects.get(username=username, password=password)
                print("can get")
                # response = HttpResponseRedirect('/ShowNews/')
                # response.set_cookie('username', username, 3600)   # 3600 is a number of cookie's valid period
                return HttpResponse('Welcome!')
            except ObjectDoesNotExist:
                return HttpResponseRedirect('/login/', {'uf': uf})
    else:
        print("login")
        uf = UserLoginForm()
        return render_to_response('login.html', {'uf': uf})