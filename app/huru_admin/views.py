from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.models import Group
from django.http import HttpResponse
from django.contrib import messages
from django.shortcuts import render
from app.main.models import Article, Testimony, Service
from django.views import View, generic
from resizeimage import resizeimage
from .forms import CreateArticle, CreateTestimony, CreateService
from django.urls import reverse
from PIL import Image
import datetime
import os


class Home(View):
    template_name = 'huru_admin/home.html'

    @method_decorator(login_required(login_url='/auth/'))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        context = {}
        context['title'] = 'Home'
        context['page_title'] = 'Dashboard'
        return render(request, self.template_name, context)


class ArticleView(View):

    template_name = 'huru_admin/article.html'

    @method_decorator(login_required(login_url='/auth/'))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        context = {}
        context['title'] = 'Article'
        context['page_title'] = 'article'
        context['articles'] = Article.objects.all()
        return render(request, self.template_name, context)


class AddArticle(generic.CreateView):
    model = Article
    form_class = CreateArticle
    extra_context = {'title': 'add article', 'page_title': 'add-article'}
    template_name = 'huru_admin/article_form.html'

    @method_decorator(login_required(login_url='/auth/'))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def form_valid(self, form):
        self.object = form.save(commit=False)

        # save image if is not None
        cover_photo = self.request.FILES.get('cover_photo', None)

        if cover_photo is not None:
            # resize image to height 280 with respect to width
            img = Image.open(cover_photo)

            #  resize cover photo height to be 600px
            img = resizeimage.resize_height(img, 600)

            ################################
            # generate image_new name .start
            ################################
            img_name = os.path.splitext(
                os.path.basename(cover_photo.name))[0]
            img_name = img_name.replace(' ', '')
            image_new_name = str(img_name) + \
                str(datetime.datetime.now().timestamp())
            image_new_name = image_new_name.replace('.', '')
            image_new_name = str(image_new_name)+'.png'
            ################################
            # generate image_new name ./end
            ################################

            name_path = 'cover_photo\\'+image_new_name
            namepath = 'media\\'+name_path

            # print(name_path)
            # print(namepath)

            # return HttpResponse('end')

            img.save(namepath, img.format, quality=70)

            img.close()

            # save user data
            self.object.cover_photo = name_path
            self.object.user = self.request.user

        return super().form_valid(form)

    def get_success_url(self):

        messages.add_message(self.request, messages.SUCCESS,
                             'Article was added successfully')
        return reverse('huru_admin:article')


class TestimonyView(View):
    template_name = 'huru_admin/testimony.html'

    @method_decorator(login_required(login_url='/auth/'))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        context = {}
        context['title'] = 'Testimony'
        context['page_title'] = 'testimony'
        context['testimonies'] = Testimony.objects.all()
        return render(request, self.template_name, context)


class AddTestimonyView(generic.CreateView):
    model = Testimony
    form_class = CreateTestimony
    extra_context = {'title': 'add testimony'}
    template_name = 'huru_admin/testimony_form.html'

    @method_decorator(login_required(login_url='/auth/'))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_success_url(self):

        messages.add_message(self.request, messages.SUCCESS,
                             'Testimony was added successfully')
        return reverse('huru_admin:testimony_view')


class ServiceView(View):
    template_name = 'huru_admin/service.html'

    @method_decorator(login_required(login_url='/auth/'))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        context = {}
        context['title'] = 'Service'
        context['page_title'] = 'service'
        context['services'] = Service.objects.all()
        return render(request, self.template_name, context)


class AddServiceView(generic.CreateView):
    model = Service
    form_class = CreateService
    extra_context = {'title': 'add service'}
    template_name = 'huru_admin/service_form.html'

    @method_decorator(login_required(login_url='/auth/'))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS,
                             'Service was added successfully')
        return reverse('huru_admin:service_view')
