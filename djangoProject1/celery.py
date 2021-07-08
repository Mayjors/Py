#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Author:wd
from __future__ import absolute_import, unicode_literals
import os
from celery import Celery


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangoProject1.settings')  # 设置django环境

app = Celery('djangoProject1')

app.config_from_object('django.conf:settings') #  使用CELERY_ 作为前缀，在settings中写配置

app.autodiscover_tasks(['djangoProject1'])  # 发现任务文件每个app下的task.py