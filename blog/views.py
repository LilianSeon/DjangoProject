from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, Http404
from blog.models import Article
from django.views.generic import TemplateView
from chartjs.views.lines import BaseLineChartView

def home(request):
    articles = Article.objects.all()
    return render(request, 'blog/home.html', {'dernier_articles': articles})

def view_post(request, id_post):
    article = Article.objects.get(id=id_post)
    return render(request, 'blog/post.html', {'post': article})

def notre_canard(request):
    return render(request, 'blog/notre_canard.html')

class LineChartJSONView(BaseLineChartView):
    def get_labels(self):
        return ["January", "February", "March", "April", "May", "June", "July"]

    def get_providers(self):
        return ["Poids de Nugget"]

    def get_data(self):
        return [[75, 44, 92, 11, 44, 95, 35]]


line_chart = TemplateView.as_view(template_name='line_chart.html')
line_chart_json = LineChartJSONView.as_view()