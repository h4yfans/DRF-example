import json

from django.views.generic import View
from django.http import HttpResponse
from updates.models import Update as UpdateModel
from .mixins import CSRFExemptMixin


class UpdateModelDetailAPIView(View):
    '''s
    Retrieve, Update, Delete
    '''

    def get(self, request, pk, *args, **kwargs):
        obj = UpdateModel.objects.get(pk=pk)
        json_data = obj.serialize()
        return HttpResponse(json_data, content_type='application/json')
        pass

    def post(self, request, *args, **kwargs):
        return HttpResponse({}, content_type='application/json')

    def put(self, request, *args, **kwargs):
        return HttpResponse({}, content_type='application/json')

    def delete(self, request, *args, **kwargs):
        return HttpResponse({}, content_type='application/json')


class UpdateModelListAPIView(CSRFExemptMixin, View):
    '''
    List View
    Create View
    '''

    def get(self, request, *args, **kwargs):
        qs = UpdateModel.objects.all()
        json_data = qs.serialize()
        return HttpResponse(json_data, content_type='application/json')

    def post(self, request, *args, **kwargs):
        data = json.dumps({'message': 'Unknown data'})
        return HttpResponse({}, content_type='application/json')

    def post(self, request, *args, **kwargs):
        data = json.dumps({'message': 'You cannot delete entire list'})
        return HttpResponse({}, content_type='application/json')

