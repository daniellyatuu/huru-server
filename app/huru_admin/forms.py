from django import forms
from app.main.models import Article, Testimony, Service
from django.forms.widgets import TextInput, FileInput, Textarea, Select, CheckboxInput


class CreateArticle(forms.ModelForm):
    class Meta:
        model = Article

        fields = ['title', 'sw_title', 'cover_photo', 'content', 'sw_content',
                  'category', 'belong_to', 'active', 'display_cover_photo_on_view_article']
        widgets = {
            'title': TextInput(attrs={'class': 'form-control', 'placeholder': 'enter title'}),
            'sw_title': TextInput(attrs={'class': 'form-control', 'placeholder': 'ingiza kichwa cha makala'}),
            'cover_photo': FileInput(attrs={'class': 'form-control', 'placeholder': 'enter cover photo'}),
            'content': Textarea(attrs={'class': 'form-control no-resize summernote',  'placeholder': 'Please type what you want...', 'rows': 40, 'style': 'display: none;'}),
            'sw_content': Textarea(attrs={'class': 'form-control no-resize summernote',  'placeholder': 'Tafadhali andika unachotaka...', 'rows': 40, 'style': 'display: none;'}),
            'belong_to': Select(attrs={'class': 'form-control show-tick'}),
            'category': Select(attrs={'class': 'form-control show-tick'}),
            'active': CheckboxInput(attrs={'id': 'checkbox'}),
            'display_cover_photo_on_view_article': CheckboxInput(attrs={'id': 'checkbox1'}),
        }


class CreateTestimony(forms.ModelForm):
    class Meta:
        model = Testimony

        fields = ['title',  'url', 'content', 'active']
        widgets = {
            'title': TextInput(attrs={'class': 'form-control', 'placeholder': 'enter title'}),
            'url': TextInput(attrs={'class': 'form-control', 'placeholder': 'enter url'}),
            'content': Textarea(attrs={'class': 'form-control no-resize',  'placeholder': 'Please type what you want...', 'rows': 40, 'id': 'summernote', 'style': 'display: none;'}),
            # 'belong_to': Select(attrs={'class': 'form-control show-tick'}),
            # 'category': Select(attrs={'class': 'form-control show-tick'}),
            'active': CheckboxInput(attrs={'id': 'checkbox'}),
        }


class CreateService(forms.ModelForm):
    class Meta:
        model = Service
        fields = ['facility', 'facility_type', 'service_offered',
                  'contact', 'region', 'district', 'location']
        widgets = {
            'facility': TextInput(attrs={'class': 'form-control', 'placeholder': 'enter facility'}),
            'facility_type': TextInput(attrs={'class': 'form-control', 'placeholder': 'enter facility type'}),
            'service_offered': Textarea(attrs={'class': 'form-control no-resize',  'placeholder': 'Enter services offered', 'rows': 40, 'id': 'summernote', 'style': 'display: none;'}),
            'contact': TextInput(attrs={'class': 'form-control', 'placeholder': 'enter contact'}),
            'region': TextInput(attrs={'class': 'form-control', 'placeholder': 'enter region'}),
            'district': TextInput(attrs={'class': 'form-control', 'placeholder': 'enter district'}),
            'location': TextInput(attrs={'class': 'form-control', 'placeholder': 'enter location'}),
        }
