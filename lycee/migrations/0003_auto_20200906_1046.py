# Generated by Django 3.0.7 on 2020-09-06 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lycee', '0002_auto_20200905_2235'),
    ]

    operations = [
        migrations.AlterField(
            model_name='presence',
            name='isMissing',
            field=models.BooleanField(default=0, help_text='is the sutdent missing ?', null=True, verbose_name='Missing ?'),
        ),
        migrations.RemoveField(
            model_name='presence',
            name='student',
        ),
        migrations.AddField(
            model_name='presence',
            name='student',
            field=models.ManyToManyField(to='lycee.Student'),
        ),
    ]
