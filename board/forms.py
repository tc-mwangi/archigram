from django import forms
from .models import Photo, Member


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control'
        }
        ))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs = {
            'class': 'form-control'
        }
        ))


class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ('image', 'caption')
        widgets = {
            'caption': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4
                })
        }


class MemberPhotoForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ('image',)