# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from forms import PostForm
from models import Post

def index(request):
	if request.method == 'POST':
		form = PostForm(request.POST)
		post = Post.objects.create(post_text=form.data['post_text'])
	form = PostForm()
	post_list = Post.objects.all()
	context = {
		'post_list': post_list,
		'form': form,
	}
	return render(request, 'index.html', context)
