# Generated by Django 2.2.9 on 2020-10-27 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inicio', '0010_auto_20201027_1501'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='libro',
            options={'verbose_name_plural': 'libros'},
        ),
        migrations.AlterField(
            model_name='donativo',
            name='archivo',
            field=models.FileField(blank=True, null=True, upload_to='media/'),
        ),
    ]
