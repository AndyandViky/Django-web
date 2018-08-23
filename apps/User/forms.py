
# _*_ coding:utf-8 _*_

from django import forms


class LoginForms(forms.Form):
    username = forms.CharField(required=True,max_length=20)
    password = forms.CharField(required=True,min_length=5)


class RegisterForms(forms.Form):
    username = forms.CharField(required=True,max_length=20)
    password1 = forms.CharField(required=True,min_length=5)
    password2 = forms.CharField(required=True,min_length=5)


class ForgetForms(forms.Form):
    pass


class ChangePwForms(forms.Form):
    password1 = forms.CharField(required=True,min_length=5)
    password2 = forms.CharField(required=True,min_length=5)