from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.http import HttpResponse
from django.contrib import messages
from django.shortcuts import render
from django.views import View
from .forms import LoginForm


class UserLogin(LoginView):

    extra_context = {'title': 'login'}
    form_class = LoginForm

    def get_success_url(self):

        user_name = self.request.user
        print(user_name)
        # if user_name is None:
        #     user_name = self.request.user.email
        # name = str(user_name).capitalize().strip()
        # messages.success(self.request, f'Hello {name}, welcome to EMS')
        return super().get_success_url()


class UserLogout(LogoutView):
    """custom logout view"""

    def get_next_page(self):
        messages.add_message(self.request, messages.SUCCESS,
                             'You successfully log out!')
        return super().get_next_page()
