# Generated by Django 4.1.5 on 2023-01-27 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DeafultApp', '0005_shoppingproducts'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShopProducts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imageurl', models.TextField()),
                ('title', models.CharField(max_length=50)),
                ('text', models.CharField(max_length=100)),
                ('price', models.FloatField()),
                ('category', models.CharField(max_length=100)),
                ('ostcategory', models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='ShoppingProducts',
        ),
    ]