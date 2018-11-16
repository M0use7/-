"""__author__ = 唐宏进 """
from django.http import HttpResponseRedirect
from django.urls import reverse


def login_required(func):

    def check_login(request):
        try:
            request.session['user_id']
        except Exception as e:
            return HttpResponseRedirect(reverse('user:login'))
        return func(request)
    return check_login
