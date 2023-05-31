from django.db import models

class HomeCarousel(models.Model):
    #Carousel banner
    imageurl=models.TextField()
    title1=models.CharField(max_length=100)
    title2=models.CharField(max_length=200)
    text=models.TextField()

    def __str__(self):
        return self.title1

class HomeCategories(models.Model):
    imageCategory = models.TextField()
    titleCategory = models.CharField(max_length=50)

    def __str__(self):
        return self.titleCategory



class FeaturedProduct(models.Model):
    imageUrl=models.TextField()
    title=models.CharField(max_length=200)
    text=models.TextField()
    price=models.FloatField()

    def __str__(self):
        return self.title


class ShopCategory(models.Model):
    categoryname=models.CharField(max_length=100)

    def __str__(self):
        return self.categoryname

class ShopOstCategory(models.Model):
    ostcategoryname=models.CharField(max_length=100)
    categorytype=models.ForeignKey(ShopCategory,on_delete=models.CASCADE)

    def __str__(self):
        return self.ostcategoryname


class ShopProducts(models.Model):
    title=models.CharField(max_length=100)
    text=models.TextField()
    ostcategorytype = models.ForeignKey(ShopOstCategory,on_delete=models.CASCADE,null=True)
    imageproduct=models.TextField()
    price=models.FloatField()

    def __str__(self):
        return self.title
