# Generated by Django 3.0.8 on 2020-08-02 22:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_blog', '0002_auto_20200801_1831'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='descripcion',
            field=models.CharField(max_length=600, verbose_name='descripcion'),
        ),
        migrations.AlterField(
            model_name='post',
            name='imagen',
            field=models.URLField(max_length=500),
        ),
        migrations.AlterField(
            model_name='post',
            name='titulo',
            field=models.CharField(max_length=200, verbose_name='Titulo'),
        ),
    ]
