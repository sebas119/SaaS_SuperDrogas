# Generated by Django 2.1.8 on 2019-08-19 23:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrador', '0008_auto_20190819_1702'),
    ]

    operations = [
        migrations.AlterField(
            model_name='role',
            name='user_type',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Administrador'), (2, 'Vendedor'), (3, 'Cliente Online')], default=3, primary_key=True, serialize=False),
        ),
    ]
