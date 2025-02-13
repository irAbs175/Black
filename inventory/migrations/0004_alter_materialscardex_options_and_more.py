# Generated by Django 4.2.3 on 2023-07-23 01:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0003_materialscardex_quantity_productscardex_quantity'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='materialscardex',
            options={'verbose_name': 'کاردکس', 'verbose_name_plural': 'کاردکس مواد اولیه'},
        ),
        migrations.AlterModelOptions(
            name='productscardex',
            options={'verbose_name': 'کاردکس', 'verbose_name_plural': 'کاردکس کالاها'},
        ),
        migrations.AddField(
            model_name='materialscardex',
            name='row',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='productscardex',
            name='row',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
