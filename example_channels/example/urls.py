from django.urls import path
from .views import log_in, log_out, user_list, sign_up

urlpatterns = [
    path('log_in', log_in, name='log_in'),
    path('log_out', log_out, name='log_out'),
    path('', user_list, name='user_list'),
    path('sign_up', sign_up, name='sign_up'),
]
