#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from django.http import JsonResponse, HttpResponse
from djangoProject1 import tasks


# Create your views here.


def index(request, *args, **kwargs):
    res = tasks.add.delay(1, 3)
    print res

    # redis 报错  celery报错 []} 86400) of pipeline caused error: value is not an integer or out of range
    # 见 https: // blog.csdn.net / m0_55837832 / article / details / 116494819

    # 任务逻辑
    # return HttpResponse("Hello world ! {}", res)
    return JsonResponse({'status': 'successful', 'task_id': res.task_id})

