# Generated by Django 4.2 on 2023-04-20 14:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BookAuthor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=50)),
                ('about_author', models.TextField(blank=True)),
                ('photo', models.ImageField(upload_to='images/')),
            ],
        ),
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_title', models.CharField(max_length=150)),
                ('publisher', models.CharField(max_length=50)),
                ('pages', models.CharField(max_length=10)),
                ('language', models.CharField(max_length=50)),
                ('book_image', models.ImageField(upload_to='images/')),
                ('authorAdd', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='books.bookauthor')),
            ],
        ),
    ]
