# Generated by Django 4.1.7 on 2023-03-23 17:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='email address')),
                ('is_active', models.BooleanField(default=True)),
                ('staff', models.BooleanField(default=False)),
                ('admin', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Candidate',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='candidate', serialize=False, to=settings.AUTH_USER_MODEL)),
                ('name', models.CharField(blank=True, max_length=256, null=True)),
                ('mobile', models.CharField(blank=True, max_length=256, null=True)),
            ],
            options={
                'verbose_name': 'Candidate',
                'verbose_name_plural': 'Candidates',
            },
            bases=('accounts.user',),
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='organization', serialize=False, to=settings.AUTH_USER_MODEL)),
                ('organization_name', models.CharField(blank=True, max_length=256, null=True)),
                ('name', models.CharField(blank=True, max_length=256, null=True)),
            ],
            options={
                'verbose_name': 'Organization',
                'verbose_name_plural': 'Organizations',
            },
            bases=('accounts.user',),
        ),
    ]
