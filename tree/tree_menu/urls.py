from django.urls import path

from tree_menu.views import IndexPageView


app_name = 'menu'

urlpatterns = [
    path('menu/', IndexPageView.as_view(), name='index')
]