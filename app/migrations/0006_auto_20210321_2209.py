# Generated by Django 3.1.7 on 2021-03-21 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_remove_article_slug'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tag',
            options={'verbose_name': 'Tags', 'verbose_name_plural': 'Tags'},
        ),
        migrations.AddField(
            model_name='tag',
            name='name',
            field=models.CharField(default='general', max_length=100, unique=True, verbose_name='Name'),
        ),
    ]