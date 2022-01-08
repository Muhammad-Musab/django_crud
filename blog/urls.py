from os import name
from django.urls import path
from django.urls.conf import include
from .views import BlogDelete, BlogView, BlogDetail, BlogCreate, BlogUpdate
urlpatterns = [
    path('', BlogView.as_view(), name='home'),
    path('post/<int:pk>/', BlogDetail.as_view(), name = 'detail-page'),
    path('post/new/', BlogCreate.as_view(), name = "blog-create"),
    path('post/<int:pk>/edit/', BlogUpdate.as_view(), name = "blog-update"),
    path('post/<int:pk>/delete/', BlogDelete.as_view(), name="blog-delete"),
]
