#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from django.http import JsonResponse, HttpResponse
from djangoProject1 import tasks


# Create your views here.


def index(request, *args, **kwargs):
    res = tasks.add.delay(1, 3)
    print res
    # 任务逻辑
    # return HttpResponse("Hello world ! {}", res)
    return JsonResponse({'status': 'successful', 'task_id': res.task_id})

