# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from datetime import datetime
from django.shortcuts import redirect
from django.template.loader import get_template
from django import template
# from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
# Create your views here.

def homepage(request):
	template=get_template('index.html')
	posts=Post.objects.all()
	now=datetime.now()
	html=template.render(locals())
	return HttpResponse(html)
	"""
	post_lists=list()
	for count,post in enumerate(posts):
		post_lists.append("No.{}:".format(str(count))+str(post).decode('utf-8')+"<br>")
		# 这里要用decode（）
		post_lists.append("<small>"+str(post.body.encode('utf-8')).decode('utf-8')+"</small><br><br><br>")
	return HttpResponse(post_lists)
	"""

def showpost(request,slug):
	template=get_template('post.html')
	# 用ppost.html来做为渲染模板
	try:
		post=Post.objects.get(slug=slug)
		if post != None:
			html=template.render(locals())
			# 找到所有内存中的变量就会找到需要渲染的东西
			return HttpResponse(html)
	except Exception as e:
		return redirect('/')