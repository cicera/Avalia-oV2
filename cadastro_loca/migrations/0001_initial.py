# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations

class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Nome', models.CharField(max_length=100, verbose_name=b'Nome')),
                ('DataNascimento', models.DateField(verbose_name=b'Data de Nascimento')),
                ('CPF', models.CharField(max_length=15, verbose_name=b'CPF')),
                ('Email', models.EmailField(max_length=100, verbose_name=b'Endere\xc3\xa7o de email')),
                ('Sexo', models.CharField(max_length=1, verbose_name=b'Sexo', choices=[(b'M', b'Masculino'), (b'F', b'Feminino')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
