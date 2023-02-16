from django.urls import path

from payments import views

from django.views.generic import TemplateView

urlpatterns = [
    path('', views.ShopListView.as_view(), name='main_page'),
    path('buy/<int:id>/', views.buy, name='buy'),
    path('item/<int:id>/', views.item, name='item'),
    path('success/', TemplateView.as_view(template_name='success.html'), name='success'),
    path('cancel/', TemplateView.as_view(template_name='cancel.html'), name='cancel'),
]
