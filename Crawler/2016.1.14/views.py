# coding:utf-8
from django.shortcuts import render_to_response
import simplejson
from gushi.models import User, AudioInfo
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
            username = uf.cleaned_data['username']  # cleaned_data 就是读取表单返回的值，返回类型为字典dict型
            password = uf.cleaned_data['password']
            email = uf.cleaned_data['email']
            # 将表单写入数据库
            try:
                username = User.objects.get(username=username)
                print("这个用户已经存在 需要再写一个html")
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
        return render_to_response('register.html', {'uf': uf}, context_instance=RequestContext(request))


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
                response = HttpResponseRedirect('/homepage/')
                # response.set_cookie('username', username, 3600)   # 3600 is a number of cookie's valid period
                # return HttpResponse('Welcome!')
                return response
            except ObjectDoesNotExist:
                return HttpResponseRedirect('/login/', {'uf': uf})
    else:
        print("login")
        uf = UserLoginForm()
        return render_to_response('login.html', {'uf': uf}, context_instance=RequestContext(request))


# homepage
class HomepageForm(forms.Form):
    audio_title = forms.CharField()
def homepage(request):
    if request.method == 'POST':
        print ("post")
        audio_title = request.POST
        # return HttpResponse("Welcome!")
        try:
            audio = AudioInfo.objects.get(title=audio_title)
            response = HttpResponseRedirect('/player/')
            return response
        except ObjectDoesNotExist:
            return HttpResponseRedirect('/homepage/')


    else:
        lists = AudioInfo.objects.all()
        return render_to_response('homepage.html', {'lists': lists})


# 播放页
def player(request):
    list = AudioInfo.objects.get(id=1)
    # audio_data = open("/home/chris/Download/story/mp3/0.mp3", "rb").read()
    audio_data = open(list.mp3_path, "rb").read()
    return HttpResponse(audio_data, "list.mp3_path")

# def audio(request):

    # image_data = open("/home/chris/Download/story/mp3/0.mp3", "rb").read()
    # return HttpResponse(image_data, content_type="0.mp3")


def test(req):
    if req.method == 'POST':
        print req.body

        data = {"error_code":0,"reason":"success","data":{"audioUrl":"http://192.168.235.52:8000/player/"}}
        data2 = simplejson.dumps(data)
        return HttpResponse(data2)