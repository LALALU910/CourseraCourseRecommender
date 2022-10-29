# Generated by Django 4.0.2 on 2022-10-25 15:26

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('course_id', models.IntegerField(primary_key=True, serialize=False)),
                ('course_name', models.CharField(max_length=256)),
                ('university_name', models.CharField(max_length=256)),
                ('course_language', models.CharField(max_length=256)),
                ('course_rating', models.FloatField()),
                ('course_level', models.CharField(max_length=256)),
                ('course_detail', models.TextField()),
                ('course_skills', models.CharField(max_length=256)),
                ('course_link', models.URLField(default='https://www.coursera.org/')),
                ('course_image', models.URLField(default='https://is4-ssl.mzstatic.com/image/thumb/Purple122/v4/26/af/93/26af935f-f1bf-0c1d-22ac-fdf72bdc3609/AppIcon-0-1x_U007emarketing-0-7-0-0-85-220-0.png/1200x630wa.png')),
                ('reco_course_id', models.CharField(max_length=256)),
            ],
            options={
                'verbose_name': 'Course Info Table',
                'db_table': 'course',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('level', models.CharField(max_length=50)),
                ('skills', models.CharField(max_length=256)),
                ('language', models.CharField(max_length=50)),
                ('university', models.CharField(max_length=256)),
                ('reco_course_id', models.CharField(max_length=256)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'User Info Table',
                'db_table': 'user',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
