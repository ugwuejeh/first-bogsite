# Generated by Django 4.2.4 on 2023-11-01 10:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile', models.ImageField(upload_to='image')),
                ('display_name', models.CharField(max_length=200)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('slug', models.SlugField(blank=True, max_length=300, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('body', models.TextField(max_length=1000)),
                ('upload_image', models.ImageField(upload_to='post')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateField(auto_now=True)),
                ('status', models.CharField(choices=[('pending', 'pending'), ('delete', 'delete'), ('approved', 'approved')], default='pending', max_length=300)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bloghome.category')),
            ],
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_body', models.TextField(max_length=400)),
                ('commenter_name', models.TextField(max_length=400)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('Post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='bloghome.post')),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='bloghome.author')),
            ],
        ),
    ]
