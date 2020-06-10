from django.shortcuts import render
from django.http import HttpResponse
from mysite import models

def index(request):

	return render(request, "index.html", locals())

def page(request, pno):
	authors = [
		'王小明', 
		'林小華', 
		'陳小毛',
		'曾小花'
	]
	if pno>=0 and pno<len(authors):
		author = authors[pno]
	else:
		author = "未知成員"
	return HttpResponse("成員簡介：{}".format(author))

def db(request, sno):
	stories = models.Story.objects.filter(sno=sno)
	if len(stories)>=1:
		story = stories[0]
	else:
		story = "找不到！"
	return HttpResponse(story)

