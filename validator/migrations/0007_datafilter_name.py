# Generated by Django 2.1 on 2018-10-07 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('validator', '0006_auto_20181006_1753'),
    ]

    operations = [
        migrations.AddField(
            model_name='datafilter',
            name='name',
            field=models.CharField(default='FIL_ALL_VALID_RANGE', max_length=30),
            preserve_default=False,
        ),
    ]