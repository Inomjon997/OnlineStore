from django.shortcuts import render
from django.views.generic import TemplateView
from .models import HomeCarousel,HomeCategories,FeaturedProduct,ShopProducts,ShopCategory,ShopOstCategory

# Create your views here.

class HomePage(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['carousel'] = HomeCarousel.objects.all()
        context['category'] = HomeCategories.objects.all()
        context['feature'] = FeaturedProduct.objects.all()
        return context


class AboutPage(TemplateView):
    template_name = 'about.html'

class ContactPage(TemplateView):
    template_name = 'contact.html'

class ShopPage(TemplateView):
    template_name = 'shop.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['prod'] = ShopProducts.objects.all()
        context['categ'] = ShopCategory.objects.all()
        context['ostcateg'] = ShopOstCategory.objects.all()
        return context