# Generated by Django 4.0.3 on 2022-04-12 08:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=100)),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='URL')),
            ],
            options={
                'verbose_name': 'Категории',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Year',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(max_length=100, verbose_name='Издана в')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='URL')),
            ],
            options={
                'verbose_name': 'Год издания',
                'verbose_name_plural': 'Год издания',
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название')),
                ('content', models.TextField(blank=True, verbose_name='Контент')),
                ('photo', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('time_create', models.DateTimeField(auto_now_add=True, verbose_name='Время создания')),
                ('time_update', models.DateTimeField(auto_now=True)),
                ('is_published', models.BooleanField(default=True, verbose_name='Опубликовано')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='URL')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='women.category')),
                ('year', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='women.year')),
            ],
            options={
                'verbose_name': 'Книги',
                'verbose_name_plural': 'Книги',
                'ordering': ['time_create', 'title', 'year', 'category'],
            },
        ),
    ]
