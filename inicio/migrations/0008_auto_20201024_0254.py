# Generated by Django 2.2.9 on 2020-10-24 02:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inicio', '0007_auto_20201024_0223'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prestamo',
            name='fecha_entrega',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='prestamo',
            name='fecha_prestamo',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='prestamo',
            name='notas',
            field=models.CharField(max_length=200),
        ),
    ]
