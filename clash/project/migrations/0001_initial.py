# Generated by Django 3.1 on 2021-02-11 23:54

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
            name='Questions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_level', models.CharField(blank=True, max_length=225)),
                ('question', models.CharField(blank=True, max_length=500)),
                ('option_A', models.CharField(blank=True, max_length=255)),
                ('option_B', models.CharField(blank=True, max_length=255)),
                ('option_C', models.CharField(blank=True, max_length=255)),
                ('option_D', models.CharField(blank=True, max_length=255)),
                ('correct_answer', models.CharField(blank=True, max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Response',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('selected_answer', models.CharField(blank=True, max_length=255)),
                ('score', models.IntegerField(default=0)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.questions')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.IntegerField(default=0)),
                ('level', models.CharField(default='fe', max_length=15)),
                ('language', models.CharField(max_length=15)),
                ('total_score', models.IntegerField(default=0)),
                ('quelist', models.TextField(default='[]', max_length=255)),
                ('marks', models.IntegerField(default=1)),
                ('status', models.BooleanField(default=True)),
                ('logouttime', models.DateTimeField(blank=True, default=None, null=True)),
                ('extra_time', models.IntegerField(default=0)),
                ('time_rem', models.IntegerField(default=1680)),
                ('get_chance', models.IntegerField(default=0)),
                ('queflist', models.TextField(default='[]', max_length=255)),
                ('quefulllist', models.TextField(default='[]', max_length=255)),
                ('visionlst', models.TextField(default='[]', max_length=255)),
                ('spin_wheel', models.BooleanField(default=False)),
                ('checkpoint', models.IntegerField(default=0)),
                ('flag', models.IntegerField(default=-1)),
                ('freezetimestart', models.DateTimeField(blank=True, default=None, null=True)),
                ('flashblind', models.IntegerField(default=0)),
                ('spincount', models.IntegerField(default=2)),
                ('progress', models.IntegerField(default=0)),
                ('getassured', models.BooleanField(default=False)),
                ('freezebar', models.BooleanField(default=False)),
                ('allow', models.BooleanField(default=False)),
                ('predicted_score', models.IntegerField(default=0)),
                ('correct_answered', models.IntegerField(default=0)),
                ('length', models.IntegerField(default=0)),
                ('freezeflag', models.IntegerField(default=0)),
                ('refresh', models.IntegerField(default=0)),
                ('permit', models.IntegerField(default=1)),
                ('tab', models.IntegerField(default=4)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
