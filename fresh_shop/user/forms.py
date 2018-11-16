"""__author__ = 唐宏进 """
from django import forms

from user.models import User


class UserRegisterForm(forms.Form):
    username = forms.CharField(required=True, max_length=20,
                               error_messages={
                                   'required': '用户名必填',
                                   'max_length': '用户名不能超过20个字符'
                               })
    password = forms.CharField(required=True,
                               error_messages={
                                   'required': '密码必填'
                               })
    password2 = forms.CharField(required=True,
                               error_messages={
                                   'required': '确认密码必填'
                               })
    email = forms.CharField(required=True,max_length=20,
                                error_messages={
                                    'required': '邮箱必填',
                                    'max_length': '邮箱不能超过20个字符'
                                })

    def clean(self):
        user = User.objects.filter(username=self.cleaned_data.get('username')).first()
        if user:
            raise forms.ValidationError({'username': '该用户已被注册'})
        if self.cleaned_data.get('password') != self.cleaned_data.get('password2'):
            raise forms.ValidationError({'password': '密码不一致'})
        return self.cleaned_data


class UserLoginForm(forms.Form):
    username = forms.CharField(required=True,
                               error_messages={
                                   'required': '用户名必填'
                               })
    password = forms.CharField(required=True,
                               error_messages={
                                   'required': '密码必填'
                               })

    def clean(self):
        user = User.objects.filter(username=self.cleaned_data.get('username')).first()
        if not user:
            raise forms.ValidationError({'username': '用户名不存在'})
        return self.cleaned_data


class UserAddressForm(forms.Form):
    # 用户地址保存的表单验证
    signer_name = forms.CharField(required=True, error_messages={'required': '收件人必填'})
    address = forms.CharField(required=True, error_messages={'required': '详细地址必填'})
    signer_mobile = forms.CharField(required=True, error_messages={'required': '收件人手机号码必填'})
    signer_postcode = forms.CharField(required=True, error_messages={'required': '邮编必填'})