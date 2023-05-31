from django.contrib import admin
from .models import HomeCarousel,HomeCategories,FeaturedProduct,ShopProducts,ShopCategory,ShopOstCategory

# Register your models here.
admin.site.register(HomeCarousel)
admin.site.register(HomeCategories)
admin.site.register(FeaturedProduct)
admin.site.register(ShopCategory)
admin.site.register(ShopOstCategory)
admin.site.register(ShopProducts)