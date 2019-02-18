from django.core.serializers import serialize
from django.views.generic import View
from django.http import HttpResponse, JsonResponse
import json

from restapi.mixins import JsonResponseMixin
from updates.models import Update


def json_example_view(request):
    data = {
        'count': 1000,
        'content': 'Some new content'
    }
    json_data = json.dumps(data)
    return HttpResponse(json_data, content_type='application/json')


class JsonCBV(View):
    def get(self, request, *args, **kwargs):
        data = {
            'count': 1000,
            'content': 'class based view'
        }
        return JsonResponse(data)


class JsonCBV2(JsonResponseMixin, View):
    def get(self, request, *args, **kwargs):
        data = {
            'count': 1000,
            'content': 'class based view'
        }
        return self.render_to_json_response(data)


class SerializedDetailView(JsonResponseMixin, View):
    def get(self, request, *args, **kwargs):
        obj = Update.objects.get(id=1)
        data = {
            'user': obj.user.username,
            'content': obj.content
        }
        json_data = json.dumps(data)
        return HttpResponse(json_data, content_type='application/json')


class SerializedListView(JsonResponseMixin, View):
    def get(self, request, *args, **kwargs):
        qs_update = Update.objects.all()
        data = serialize('json', qs_update, fields=('user', 'content'))
        print(data)
        return HttpResponse(data, content_type='application/json')
