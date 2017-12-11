# -*- coding: utf-8 -*-
from __future__ import unicode_literals


# Create your views here.
from django.http import JsonResponse


def update_info(request):
    attr = request.GET.get('attr', None)
    new_val = request.GET.get('new_val', None)
    try:
        setattr(request.user.profile, attr, new_val)
        request.user.profile.save()
        return JsonResponse({'status': 'Success', 'msg': 'save successfully'})
    except TypeError:
        return JsonResponse({'status':'Fail', 'msg': 'empty request'})