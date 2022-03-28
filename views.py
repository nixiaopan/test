import json
import logging

from django.http import JsonResponse
from wxcloudrun.models import Counters
from django.http import HttpResponse

logger = logging.getLogger('log')




def test1(request):
    """
    获取当前计数
    """
    logger.info('update_count req: {}'.format(request.body))
    return HttpResponse(json.dumps({'1':"2"}))
    # return JsonResponse({'code': 0, 'data': 0}, json_dumps_params={'ensure_ascii': False})


