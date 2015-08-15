# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pessoa', '0003_pessoa_ano'),
    ]

    operations = [
        migrations.CreateModel(
            name='Telefone',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('telefone', models.CharField(max_length=9)),
                ('pessoa', models.ForeignKey(to='pessoa.Pessoa')),
            ],
        ),
    ]
