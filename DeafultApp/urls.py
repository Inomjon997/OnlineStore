from django.urls import path
from .views import HomePage,AboutPage,ContactPage,ShopPage

urlpatterns=[
    path('',HomePage.as_view(),name='home'),
    path('about',AboutPage.as_view(),name='about'),
    path('contact',ContactPage.as_view(),name='contact'),
    path('shop',ShopPage.as_view(),name='shop'),
]