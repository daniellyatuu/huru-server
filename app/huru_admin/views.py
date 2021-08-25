from .forms import CreateArticle, CreateTestimony, CreateService
from django.contrib.auth.decorators import login_required
from app.main.models import Article, Testimony, Service
from django.utils.decorators import method_decorator
from django.contrib.auth.models import Group
from django.http import HttpResponse
from django.contrib import messages
from django.shortcuts import render
from django.views import View, generic
from app.user.models import User
from resizeimage import resizeimage
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
        context['articles_no'] = Article.objects.all().count()
        context['users_no'] = User.objects.all().count()
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

        # ################################
        # # RESIZE IMAGE .START
        # ################################
        cover_photo = self.request.FILES.get('cover_photo', None)

        # # resize image (800px * 800px)
        # img = Image.open(cover_photo)
        #
        # # check image size
        # width = img.size[0]
        # height = img.size[1]
        #
        # aspect = width / float(height)
        #
        # ideal_width = 800
        # ideal_height = 800
        #
        # ideal_aspect = ideal_width / float(ideal_height)
        #
        # if aspect > ideal_aspect:
        #     # Then crop the left and right edges:
        #     new_width = int(ideal_aspect * height)
        #     offset = (width - new_width) / 2
        #     resize = (offset, 0, width - offset, height)
        # else:
        #     # ... crop the top and bottom:
        #     new_height = int(width / ideal_aspect)
        #     offset = (height - new_height) / 2
        #     resize = (0, offset, width, height - offset)
        #
        # img = img.crop(resize).resize(
        #     (ideal_width, ideal_height), Image.ANTIALIAS)
        #
        # # generate image_new name .start
        # filename, file_extension = os.path.splitext(cover_photo.name)
        #
        # filename = filename.replace(' ', '')
        # new_filename = str(filename) + \
        #     str(datetime.datetime.now().timestamp())
        #
        # new_filename = new_filename.replace('.', '')
        # new_filename = str(new_filename)+str(file_extension)
        # # generate image_new name ./end
        #
        # # name_path = 'cover_photo/'+new_filename
        # # namepath = 'media/'+name_path
        #
        # name_path = os.path.join('cover_photo', new_filename)
        # namepath = os.path.join('media', name_path)
        #
        # img.save(namepath, img.format, quality=90)
        # img.close()
        #
        # ################################
        # # RESIZE IMAGE .END
        # ################################
        #
        self.object.cover_photo = cover_photo
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
