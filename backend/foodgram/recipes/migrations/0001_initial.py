# Generated by Django 2.2.19 on 2022-08-12 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Название')),
                ('amount', models.FloatField(verbose_name='Количество')),
                ('measurement_unit', models.CharField(max_length=50, verbose_name='Единица измерения')),
            ],
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Название')),
                ('image', models.ImageField(upload_to='recipes/', verbose_name='Картинка')),
                ('text', models.TextField(verbose_name='Описание')),
                ('cooking_time', models.PositiveIntegerField(verbose_name='Время приготовления')),
                ('pub_date', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Дата публикации')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True, verbose_name='Название')),
                ('color', models.CharField(max_length=50, unique=True, verbose_name='Цветовой HEX-код')),
                ('slug', models.SlugField(unique=True, verbose_name='Идентификатор')),
            ],
        ),
    ]
