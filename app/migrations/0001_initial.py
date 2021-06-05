# Generated by Django 3.2.4 on 2021-06-05 14:46

import app.helper
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=256)),
                ('last_name', models.CharField(max_length=256)),
                ('username', models.CharField(max_length=256, unique=True)),
                ('phone_number', models.CharField(max_length=80, unique=True, validators=[django.core.validators.RegexValidator('^\\+\\d{1,3}\\d{3,}$', 'Make sure you add valid a phone number. Add country code in number e.g +234XXXX', 'invalid phone number')])),
                ('email', models.CharField(blank=True, max_length=80, null=True)),
                ('date_of_birth', models.DateField()),
                ('gender', models.CharField(choices=[('m', 'Male'), ('f', 'Female'), ('o', 'Other')], default='o', max_length=10)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'account',
                'verbose_name_plural': 'accounts',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('slug', models.SlugField(unique=True)),
                ('image', models.ImageField(default='', upload_to=app.helper.scramble_uploaded_image)),
                ('height_field', models.IntegerField(default=0)),
                ('width_field', models.IntegerField(default=0)),
                ('content', models.TextField()),
                ('draft', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='app.account')),
            ],
            options={
                'verbose_name': 'post',
                'verbose_name_plural': 'posts',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.post')),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='app.account')),
            ],
            options={
                'verbose_name': 'comment',
                'verbose_name_plural': 'comments',
            },
        ),
    ]