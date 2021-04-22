# Generated by Django 2.2.4 on 2021-04-22 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transact', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='date',
            field=models.DateField(auto_now=True),
        ),
        migrations.AddField(
            model_name='transaction',
            name='type',
            field=models.CharField(default='A', max_length=1),
            preserve_default=False,
        ),
    ]