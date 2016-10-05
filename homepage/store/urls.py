from django.conf.urls import url
from store import views

urlpatterns = [
    url(r'^$', views.product_list, name='product_list'),
]