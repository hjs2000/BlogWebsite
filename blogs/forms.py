from django import forms
from django.forms import widgets
from django.core.exceptions import ValidationError
from blogs import models

class RegisterForm(forms.Form):
    username = forms.CharField(max_length=150,label='用户名',
        widget=widgets.TextInput(attrs={'class':'form-control'}),
        error_messages={'max_length': '最长是16', 'min_length': '最短是3', 'required': '这个必须填'})
    password = forms.CharField(max_length=150,label='密码',
        widget=widgets.PasswordInput(attrs={'class':'form-control'}),
        error_messages={'max_length': '最长是16', 'min_length': '最短是6', 'required': '这个必须填'})
    re_password = forms.CharField(max_length=150,  label='确认密码',
        widget=widgets.PasswordInput(attrs={'class': 'form-control'}),
        error_messages={'max_length': '最长是16', 'min_length': '最短是6', 'required': '这个必须填'})
    email = forms.EmailField(label='邮箱',widget=widgets.TextInput(attrs={'class': 'form-control'}),required=False,
        error_messages={'required': '这个必须填', 'invalid': '不符合邮箱格式'})
    
    def clean_username(self):
        name = self.cleaned_data.get('username')
        ret = models.BlogUser.objects.filter(username=name).first()
        if ret:
            print("注册表单,用户名已存在")
            raise ValidationError('用户名已存在')
        return name

    def clean(self):
        pwd = self.cleaned_data.get('password')
        re_pwd = self.cleaned_data.get('re_password')
        if pwd and re_pwd:
            if pwd == re_pwd:
                return self.cleaned_data
            else:
                print("注册表单,两次密码不一致")
                raise ValidationError('两次密码不一致')

class LoginForm(forms.Form):
    username = forms.CharField(max_length=150,label='用户名',
        widget=widgets.TextInput(attrs={'class':'form-control'}),
        error_messages={'max_length': '最长是16', 'min_length': '最短是3', 'required': '这个必须填'})
    password = forms.CharField(max_length=150,label='密码',
        widget=widgets.PasswordInput(attrs={'class':'form-control'}),
        error_messages={'max_length': '最长是16', 'min_length': '最短是6', 'required': '这个必须填'})

class ForgetPasswordForm(forms.Form):
    username = forms.CharField(max_length=150,label='用户名',
        widget=widgets.TextInput(attrs={'class':'form-control'}),
        error_messages={'max_length': '最长是16', 'min_length': '最短是3', 'required': '这个必须填'})
    password = forms.CharField(max_length=150,label='密码',
        widget=widgets.PasswordInput(attrs={'class':'form-control'}),
        error_messages={'max_length': '最长是16', 'min_length': '最短是6', 'required': '这个必须填'})
    re_password = forms.CharField(max_length=150,  label='确认密码',
        widget=widgets.PasswordInput(attrs={'class': 'form-control'}),
        error_messages={'max_length': '最长是16', 'min_length': '最短是6', 'required': '这个必须填'})
    email = forms.EmailField(label='邮箱',widget=widgets.TextInput(attrs={'class': 'form-control'}),required=False,
        error_messages={'required': '这个必须填', 'invalid': '不符合邮箱格式'})
    