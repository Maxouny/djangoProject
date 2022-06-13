from django.shortcuts import render
from django.http import HttpResponse
from myblog.models import Article


# Create your views here.
def home(request):
    posts = Article.objects.order_by('created_at')
    return render(request, 'mybloghtml/home.html', {'posts': posts})


def test(request):
    return HttpResponse('<h1>test page</h1>')
