from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Update
import json

def update_model_detail_view(request):
    data = {
        'count': 1000,
        'content': 'Some new content'
    }
    json_data = json.dumps(data)
    return HttpResponse(json_data, content_type='application/json')
