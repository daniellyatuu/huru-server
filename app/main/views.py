from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from app.main.models import Article, Category, Testimony, Service
from django.views.generic.detail import DetailView
from django.utils.translation import gettext as _
from django.utils import translation
from django.utils.translation import get_language
from django.db.models import Q


class HomeView(View):
    template_name = 'main/home.html'

    def get(self, request, *args, **kwargs):

        # x = get_language()
        # print('language used is = ', x)

        context = {}
        context['title'] = 'Huru'
        # context['hello'] = _('hello')
        context['posts'] = Article.objects.filter(
            active=True, belong_to__name='pwud')
        context['service_number'] = Service.objects.all().count()
        context['testimonies'] = Testimony.objects.all()
        return render(request, self.template_name, context)


class HCWHomeView(View):
    template_name = 'main/hcw_home.html'

    def get(self, request, *args, **kwargs):

        context = {}
        context['title'] = 'Huru'
        context['posts'] = Article.objects.filter(
            active=True, belong_to__name='hcw')
        # context['service_number'] = Service.objects.all().count()
        # context['testimonies'] = Testimony.objects.all()
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
        context['testimonies'] = Testimony.objects.all()
        return render(request, self.template_name, context)


class BlogView(View):
    template_name = 'main/blog.html'

    def get(self, request, *args, **kwargs):
        context = {}
        context['title'] = 'Information'
        context['posts'] = Article.objects.filter(
            active=True, belong_to__name='pwud')
        return render(request, self.template_name, context)


class HcwBlogView(View):
    template_name = 'main/hcw_blog.html'

    def get(self, request, *args, **kwargs):
        context = {}
        context['title'] = 'Health Care Worker Information'
        context['posts'] = Article.objects.filter(
            active=True, belong_to__name='hcw')
        return render(request, self.template_name, context)


class BlogDetailView(DetailView):
    model = Article
    extra_context = {'title': 'Huru article'}


class HcwBlogDetailView(DetailView):
    template_name = 'main/hcw_article_detail.html'
    model = Article
    extra_context = {'title': 'Huru article'}


class CategoryDetailView(DetailView):
    model = Category
    extra_context = {'title': 'Huru category article'}


class HcwCategoryDetailView(DetailView):
    template_name = 'main/hcw_category_detail.html'
    model = Category
    extra_context = {'title': 'Huru category article'}


class ServiceView(View):
    template_name = 'main/services.html'

    def get(self, request, *args, **kwargs):

        # filter by keyword
        print('in here please')
        keyword = self.request.GET.get('keyword', '')
        print(keyword)
        queryset = Service.objects.all()
        if keyword:
            queryset = queryset.filter(Q(facility__icontains=keyword) | Q(
                facility_type__icontains=keyword))

        context = {}
        context['title'] = 'Services'
        context['services'] = queryset
        return render(request, self.template_name, context)


class TestimonyDetailView(DetailView):
    model = Testimony
    extra_context = {'title': 'Huru testimony'}
