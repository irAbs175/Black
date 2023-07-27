# Generated by Django 4.2.3 on 2023-07-27 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0006_alter_user_accounts_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_accounts',
            name='category',
            field=models.IntegerField(choices=[(0, 'پرسنل انبار اخلافی'), (1, 'پرسنل انبار پلاک ۳'), (2, 'پرسنل انبار مغازه قدیر'), (3, 'انباردار / حسابدار'), (4, 'توسعه / مدیریت')], default=0, verbose_name='دسته پرسنلی'),
        ),
    ]
