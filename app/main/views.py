from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

class HomeView(View):
    template_name = 'main/home.html'

    def get(self, request, *args, **kwargs):
        context = {}
        context['title']='Huru'
        return render(request, self.template_name, context)