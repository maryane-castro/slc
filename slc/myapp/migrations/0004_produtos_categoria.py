# Generated by Django 4.2 on 2023-04-11 22:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_produtos_name_produto'),
    ]

    operations = [
        migrations.AddField(
            model_name='produtos',
            name='categoria',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='myapp.lista'),
        ),
    ]
