# Generated by Django 2.0.5 on 2018-06-19 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('roles', '0007_bodyrole_priority'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bodyrole',
            options={'ordering': ('body__name', 'priority'), 'verbose_name': 'Body Role', 'verbose_name_plural': 'Body Roles'},
        ),
        migrations.AlterField(
            model_name='bodyrole',
            name='priority',
            field=models.IntegerField(default=0),
        ),
    ]