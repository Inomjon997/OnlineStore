# Generated by Django 4.1.5 on 2023-01-25 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DeafultApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MainCategories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imageurl', models.TextField()),
                ('title', models.CharField(max_length=50)),
            ],
        ),
    ]