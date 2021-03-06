# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-14 18:29
from __future__ import unicode_literals

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
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar', models.FileField(upload_to=b'', verbose_name='\u0410\u0432\u0430\u0442\u0430\u0440')),
                ('bio', models.TextField(blank=True, max_length=500, null=True, verbose_name='\u041e \u0441\u0435\u0431\u0435')),
                ('city', models.CharField(blank=True, max_length=30, null=True, verbose_name='\u0413\u043e\u0440\u043e\u0434')),
                ('birth_date', models.DateField(blank=True, null=True, verbose_name='\u0414\u0430\u0442\u0430 \u0440\u043e\u0436\u0434\u0435\u043d\u0438\u044f')),
                ('gender', models.CharField(choices=[[b'male', '\u041c\u0443\u0436\u0441\u043a\u043e\u0439'], [b'female', '\u0416\u0435\u043d\u0441\u043a\u0438\u0439']], default=b'male', max_length=10, verbose_name='\u041f\u043e\u043b')),
                ('relationship', models.CharField(choices=[[b'none', '\u041d\u0435 \u043e\u043f\u0440\u0435\u0434\u0435\u043b\u0435\u043d\u043d\u043e'], [b'single', '\u0425\u043e\u043b\u043e\u0441\u0442'], [b'in_a_rel', '\u0412 \u043e\u0442\u043d\u043e\u0448\u0435\u043d\u0438\u044f\u0445'], [b'engaged', '\u041f\u043e\u043c\u043e\u043b\u0432\u043b\u0435\u043d(\u0430)'], [b'married', '\u0416\u0435\u043d\u0430\u0442/\u0417\u0430\u043c\u0443\u0436\u0435\u043c'], [b'in_love', '\u0412\u043b\u044e\u0431\u043b\u0435\u043d(\u0430)'], [b'complicated', '\u0412\u0441\u0435 \u0441\u043b\u043e\u0436\u043d\u043e']], default=b'none', max_length=20, verbose_name='\u0421\u0442\u0430\u0442\u0443\u0441 \u043e\u0442\u043d\u043e\u0448\u0435\u043d\u0438\u0439')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='\u041f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044c')),
            ],
        ),
    ]
