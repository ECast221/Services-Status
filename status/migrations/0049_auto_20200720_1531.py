# Generated by Django 3.0.7 on 2020-07-20 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('status', '0048_auto_20200717_1636'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ticket',
            name='sub_service',
        ),
        migrations.AddField(
            model_name='ticket',
            name='sub_service',
            field=models.ManyToManyField(blank=True, to='status.SubService', verbose_name='Sub - Services'),
        ),
    ]
