"""squats_Assigment URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from logins.views import *
from django.views.static import serve
from django.conf import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]

#media urls
urlpatterns += [
        url(r'^media/(?P<path>.*)$', serve, {
            'document_root': settings.MEDIA_ROOT,
        }),
]


urlpatterns += [
    url(r'^$', loginLabController),
    url(r'^labLogin/$', loginLabController),
    url(r'^logout/$', logoutController),
    url(r'^register/$', registrationController),
    url(r'^posts/$', postsController),
    url(r'^savePost/$', savePostController),
    url(r'^getPostList/$', getPostListAPI),
    url(r'^usersLists/$', userController),
    url(r'^getAllUserDetails/$', getAllUserDetailsAPI),
    url(r'^searchUser/$', searchUserController),
    url(r'^searchUserDetailsAPI/$', searchUserDetailsAPI),
]