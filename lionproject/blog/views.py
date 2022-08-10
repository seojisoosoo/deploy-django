from operator import index
from django.shortcuts import render, redirect, get_object_or_404
from .models import Blog
from django.utils import timezone
from django.http import JsonResponse
import json


def home(request):
    if request.method == 'GET':
        blogs = Blog.objects.all()
        blog_list = []
        for blog in blogs:
            blog_list.append({
                'id': blog.id,
                'title': blog.title,
                'writer': blog.writer,
                'body': blog.body, })

        return JsonResponse({
            'data': blog_list
        })
    elif request.method == 'POST':
        body = json.loads(request.body.decode('utf-8'))

        blog = Blog.objects.create(
            title=body['title'],
            writer=body['writer'],
            body=body['body'],
            pub_date=timezone.now()
        )
        return JsonResponse({
            'ok': True,
            'data': {'title': blog.title,
                     'writer': blog.writer,
                     'body': blog.body, }
        })
def update(request, id):
    if request.method == 'PUT':
        body = json.loads(request.body.decode('utf-8'))

        update = get_object_or_404(Blog, pk=id)
        # update = get_object_or_404(Blog, pk=index)
        # update = Blog.objects.get(id=id)
        # update.id = body['id']
        update.title = body['title']
        update.writer = body['writer']
        update.body = body['body']
        update.pub_date = timezone.now()
        update.save()
        return JsonResponse({
            'ok': True,
            'data': {
                # 'id': update.id,
                'title': update.title,
                'writer': update.writer,
                'body': update.body, }
        })
def delete(request, id):
    if request.method == 'DELETE':
        delete = get_object_or_404(Blog, pk=id)
        # delete = Blog.objects.get(id=id-1)

        delete.delete()
        return JsonResponse({
            'ok': True,
            'data': None
        })
