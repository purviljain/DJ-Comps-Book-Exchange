# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-06-23 07:33
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('chat', '0002_auto_20180208_1856'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChatRoom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('receiver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='receiver', to=settings.AUTH_USER_MODEL)),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sender', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterModelOptions(
            name='message',
            options={'ordering': ('-timestamp',)},
        ),
        migrations.RemoveField(
            model_name='message',
            name='receiver',
        ),
        migrations.RemoveField(
            model_name='message',
            name='sender',
        ),
        migrations.AddField(
            model_name='message',
            name='conversation',
            field=models.ForeignKey(default=False, on_delete=django.db.models.deletion.CASCADE, related_name='conversation', to='chat.ChatRoom'),
        ),
    ]
