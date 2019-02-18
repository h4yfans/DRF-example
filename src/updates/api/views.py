from django.views.generic import View
from django.http import HttpResponse
from updates.models import Update as UpdateModel


class UpdateModelDetailAPIView(View):
    '''
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


class UpdateModelListAPIView(View):
    '''
    List View
    Create View
    '''

    def get(self, request, *args, **kwargs):
        qs = UpdateModel.objects.all()
        json_data = qs.serialize()
        return HttpResponse(json_data, content_type='application/json')

    def post(self, request, *args, **kwargs):
        return HttpResponse({}, content_type='application/json')
