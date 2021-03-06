# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth import logout, login, authenticate
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from logins.models import *
from logins.serializers import *
from django.template.context import RequestContext
from django.shortcuts import render
from django.utils import timezone
from django.core import serializers
from django.db.models import Q

# Create your views here.
def logoutController(request):
    request.session.flush()
    request.session.modified = True
    logout(request)
    response = HttpResponseRedirect('/')
    return response

def loginLabController(request):
    # return HttpResponse("Hello, world. You're at the polls index.")
    if request.method == "POST":
        username = request.POST.get('username')  # logic only for member login
        password = request.POST.get('pwd')

        if userDetails.objects.filter(username=username, password=password).exists():
            userObj = userDetails.objects.get(username=username, password=password)
            request.session['name'] = userObj.fullName
            request.session['userid'] = userObj.id
            resp = HttpResponseRedirect('/posts/')
            return resp
        else:
            return render(request, 'registration/login.html', {'error': '*Username or Password is invalid'})
    return render(request, 'registration/login.html', {'error': ''})


def registrationController(request):
    name = request.POST.get('uname')  # logic only for member login
    email = request.POST.get('uemail')
    contact = request.POST.get('contact')
    u_name = request.POST.get('u_name')
    user_pwd = request.POST.get('user_pwd')
    userObj = userDetails()
    userObj.fullName = name
    userObj.contact = contact
    userObj.email = email
    userObj.username = u_name
    userObj.password = user_pwd
    userObj.registeredDate = timezone.now()
    userObj.save()
    return render(request, 'registration/login.html', {'success': 'Your registration has been done successfully.'})


def postsController(request):
    return render(request, 'registration/postList.html', {'error': ''})


def userController(request):
    return render(request, 'registration/userLists.html', {'error': ''})

def searchUserController(request):
    return render(request, 'registration/searchUser.html', {'error': ''})


def savePostController(request):
    try:
        postText = request.POST.get('postText')
        userId = request.session.get('userid')
        postObj = posts()
        postObj.postText = postText
        postObj.postDate = timezone.now()
        postObj.userDetailsId_id = userId
        postObj.save()
        return HttpResponse(1)
    except:
        return HttpResponse(0)


def getPostListAPI(request):
    try:
        postList = posts.objects.all().order_by('-postDate')
        qs_json = postSerialiser(postList, many=True).data
        return JSONResponse(qs_json)
    except:
        return JSONResponse([])


def getAllUserDetailsAPI(request):
    try:
        userList = userDetails.objects.all()
        userjson = userDetailsSerialiser(userList, many=True).data
        return JSONResponse(userjson)
    except:
        return JSONResponse([])


def searchUserDetailsAPI(request):
    try:
        searchText = request.POST.get('searchText')
        query = Q(fullName__icontains=searchText) | Q(contact__icontains=searchText) | Q(email__icontains=searchText)
        userList = userDetails.objects.filter(query).values_list('id', flat=True)
        postList = posts.objects.filter(userDetailsId_id__in=userList).order_by('-postDate')
        qs_json = postSerialiser(postList, many=True).data
        return JSONResponse(qs_json)
    except:
        return JSONResponse([])


