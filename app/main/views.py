from django.shortcuts import render
from django.http import HttpResponse
from django.views import View


class HomeView(View):
    template_name = 'main/home.html'

    def get(self, request, *args, **kwargs):
        context = {}
        context['title'] = 'Huru'
        return render(request, self.template_name, context)


class AboutUsView(View):
    template_name = 'main/about_us.html'

    def get(self, request, *args, **kwargs):
        context = {}
        context['title'] = 'About us'
        return render(request, self.template_name, context)


class ContactView(View):
    template_name = 'main/contact.html'

    def get(self, request, *args, **kwargs):
        context = {}
        context['title'] = 'Contact'
        return render(request, self.template_name, context)


class TestimonyView(View):
    template_name = 'main/testimony.html'

    def get(self, request, *args, **kwargs):
        context = {}
        context['title'] = 'Testimony'
        return render(request, self.template_name, context)


class BlogView(View):
    template_name = 'main/blog.html'

    def get(self, request, *args, **kwargs):
        context = {}
        context['title'] = 'Blog'
        return render(request, self.template_name, context)
