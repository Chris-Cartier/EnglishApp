# coding:utf-8
from django.shortcuts import render
from gushi import models
from django.http import HttpResponse
import urllib
import json


def login(request):
    if request.method == 'POST':
        strs = request.body   # 表示请求的正文
        strs2 = urllib.unquote(strs)   # 将url式的数据解码
        dict = json.loads(strs2)     # 将一个json串转化为dict
        # print dict
        username = dict["user_id"]
        password = dict['password']
        username = models.User.objects.filter(user_name__exact=username)
        if username:
            user = models.User.objects.filter(user_name__exact=username, user_password__exact=password)
            if user:
                dict = {"return": "success"}
                dict_data = json.dumps(dict)    # 对数据进行JSON格式化编码
                return HttpResponse(dict_data)
            else:
                dict = {"return": "Password is wrong!"}
                dict_data = json.dumps(dict)
                return HttpResponse(dict_data)
        else:
            dict = {"return": "Users do not exist!"}
            dict_data = json.dumps(dict)
            return HttpResponse(dict_data)
    else:
        dict = {"return": "failure"}
        dict_data = json.dumps(dict)
        return HttpResponse(dict_data)


def register(request):
    if request.method == 'POST':
        str = urllib.unquote(request.body)
        dict = json.loads(str)
        username = dict["user_id"]
        password = dict['password']
        username = models.User.objects.filter(user_name__exact=username)
        if username:
            dict = {"return": "Users exist!"}
            dict_data = json.dumps(dict)
            return HttpResponse(dict_data)
        else:
            m = models.User(username, password)
            m.save()
            dict = {"return": "Succees to save!"}
            dict_data = json.dumps(dict)
            return HttpResponse(dict_data)
    else:
        dict = {"return": "failure"}
        dict_data = json.dumps(dict)
        return HttpResponse(dict_data)


# def crawl(request):
#     if request.method == 'GET':

