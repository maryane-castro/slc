# Generated by Django 4.2 on 2023-04-12 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_produtos_valor_produto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lista',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='produtos',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
