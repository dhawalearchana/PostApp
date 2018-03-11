from django.contrib.auth.models import User, Group
from logins.models import *
from rest_framework import serializers
from django.http import HttpResponseRedirect, HttpResponse
from rest_framework.renderers import JSONRenderer

class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """

    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)



class userDetailsSerialiser(serializers.ModelSerializer):
    class Meta:
        model = userDetails
        fields = '__all__'


class postSerialiser(serializers.ModelSerializer):
    userDetailsId = userDetailsSerialiser()

    class Meta:
        model = posts
        fields = '__all__'