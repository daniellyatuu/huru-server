from django import forms
from app.main.models import Article, Testimony
from django.forms.widgets import TextInput, FileInput, Textarea, Select, CheckboxInput


class CreateArticle(forms.ModelForm):
    class Meta:
        model = Article

        fields = ['title',  'cover_photo', 'content',
                  'category', 'belong_to', 'active']
        widgets = {
            'title': TextInput(attrs={'class': 'form-control', 'placeholder': 'enter title'}),
            'cover_photo': FileInput(attrs={'class': 'form-control', 'placeholder': 'enter cover photo'}),
            'content': Textarea(attrs={'class': 'form-control no-resize',  'placeholder': 'Please type what you want...', 'rows': 40, 'id': 'summernote', 'style': 'display: none;'}),
            'belong_to': Select(attrs={'class': 'form-control show-tick'}),
            'category': Select(attrs={'class': 'form-control show-tick'}),
            'active': CheckboxInput(attrs={'id': 'checkbox'}),
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
