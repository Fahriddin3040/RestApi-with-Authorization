# Generated by Django 4.2.7 on 2023-11-23 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bc', '0010_remove_category_slug_alter_category_title_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(default=0, null=True),
        ),
    ]
