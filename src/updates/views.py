from django.views.generic import View
from django.http import HttpResponse, JsonResponse
import json

from restapi.mixins import JsonResponseMixin


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
