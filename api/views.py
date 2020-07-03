from django.contrib.auth.models import Group, Permission
from django.shortcuts import render

# Create your views here.
from rest_framework.throttling import UserRateThrottle
from rest_framework.views import APIView
from rest_framework.authentication import BaseAuthentication
from rest_framework.request import Request

from api.authentications import MyAuth
from api.models import User
from api.throttle import SendMsgRate
from utils.response import APIResponse
from rest_framework import settings
from rest_framework.permissions import BasePermission, IsAuthenticated


class UserAPIView(APIView):
    def get(self,request,*args,**kwargs):
        #查询用户
        user = User.objects.first()
        # print(user)  #admin(注册的超级用户)
        #根据用户获取角色
        # print(user.groups.first())
        #根据用户获取其对应的权限
        # print(user.user_permissions.first().name) #Can add log entry

        #获取角色
        group = Group.objects.first()
        # print(group) #第一组
        #通过角色获取对应的权限
        # print(group.permissions.first())
        #通过角色获取对应的用户
        # print(group.user_set.first().username)

        #获取权限
        per = Permission.objects.filter(pk=1).first()
        print(per.name)  #Can add log entry
        #根据权限获取用户
        print(per.user_set.first().username)  #admin
        #根据权限获取角色
        print(per.group_set.first())  #第一组
        return APIResponse("SUCCESS")

class TestPessionAPIView(APIView):
    authentication_classes = [MyAuth]
    def get(self,request,*args,**kwargs):
        permission_classes = [IsAuthenticated]

        def get(self, request, *args, **kwargs):
            return APIResponse("登录访问成功")

class UserLoginOrReadOnly(APIView):
        """
        登录可写  游客只读
        """
        throttle_classes = [UserRateThrottle]

        # permission_classes = [MyPermission]

        def get(self, request, *args, **kwargs):
            return APIResponse("读操作访问成功")

        def post(self, request, *args, **kwargs):
            return APIResponse("写操作")
class SendMsgAPIView(APIView):
        throttle_classes = [SendMsgRate]

        def get(self, request, *args, **kwargs):
            return APIResponse("读操作访问成功")

        def post(self, request, *args, **kwargs):
            return APIResponse("写操作")
