from django.http import HttpResponse
from django.shortcuts import render, redirect
from artapp.models import ArtTag


# Create your views here.
def index(request):
    '''
    Desc: 首页
    :param request:request请求对象,包含请求头等信息
    :return:
        返回list.html
    '''

    return render(request, 'art/list.html', context={'name': 'stephen', 'age': 20})


def add_tags(request):
    '''
    Desc:添加标签类型的处理函数
    :param request:
    :return:
    '''
    if request.method == 'GET':
        # 请求动作:一种是新增,还有一种是修改
        return render(request, 'art/edit_tags.html')
    else:
        # POST 请求
        # 请求动作:一种是新增,还有一种是修改
        tag = ArtTag()
        tag.title = request.POST.get('title')
        tag.save()  # 保存到数据库
        return redirect('/art/list_tags')  # 重定向


def list_tags(request):
    return render(request, 'art/tags_list.html', context={
        'tags': ArtTag.objects.all()
    })
