from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request):
    '''
    Desc:
        首页
    :param request:request请求对象,包含请求头等信息
    :return:
        返回list.html
    '''

    return render(request, 'art/list.html', context={'name': 'stephen', 'age': 20})
