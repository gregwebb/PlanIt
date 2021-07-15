# Generated by Django 3.2.5 on 2021-07-15 01:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main_app', '0016_merge_0015_auto_20210714_1924_0015_auto_20210714_2238'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='activity',
            name='attendees',
        ),
        migrations.AddField(
            model_name='activity',
            name='attendees',
            field=models.ManyToManyField(related_name='attend_user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Attendees',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='activity_name', to='main_app.activity')),
                ('users', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_name', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
