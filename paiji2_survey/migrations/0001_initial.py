# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('value', models.CharField(max_length=255, verbose_name='value')),
            ],
            options={
                'verbose_name': 'choice',
                'verbose_name_plural': 'choices',
            },
        ),
        migrations.CreateModel(
            name='Poll',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255, verbose_name='title')),
                ('beginning', models.DateTimeField(default=django.utils.timezone.now, verbose_name='beginning')),
                ('end', models.DateTimeField(verbose_name='end')),
            ],
            options={
                'ordering': ('-end',),
                'get_latest_by': 'end',
                'verbose_name': 'poll',
                'verbose_name_plural': 'polls',
            },
        ),
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('choice', models.ForeignKey(related_name='votes', verbose_name='choice', to='paiji2_survey.Choice')),
                ('user', models.ForeignKey(related_name='votes', verbose_name='user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'vote',
                'verbose_name_plural': 'votes',
            },
        ),
        migrations.AddField(
            model_name='choice',
            name='poll',
            field=models.ForeignKey(related_name='choices', verbose_name='poll', to='paiji2_survey.Poll'),
        ),
        migrations.AlterUniqueTogether(
            name='vote',
            unique_together=set([('user', 'choice')]),
        ),
    ]
