# Generated by Django 4.2 on 2023-04-12 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_produtos_categoria'),
    ]

    operations = [
        migrations.AddField(
            model_name='produtos',
            name='valor_produto',
            field=models.FloatField(default=0),
        ),
    ]
