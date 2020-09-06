# Generated by Django 3.0.7 on 2020-09-05 22:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lycee', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cursus',
            name='scholar_year',
            field=models.CharField(default='0000-0001', max_length=9, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='birth_date',
            field=models.DateField(help_text='Birth date of the student', null=True, verbose_name='date of birth'),
        ),
        migrations.AlterField(
            model_name='student',
            name='email',
            field=models.EmailField(default='x@y.z', help_text='Email of the student', max_length=255, verbose_name='email'),
        ),
        migrations.AlterField(
            model_name='student',
            name='first_name',
            field=models.CharField(help_text='first name of the student', max_length=50),
        ),
        migrations.CreateModel(
            name='Presence',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reason', models.CharField(default='aucun', max_length=50, null=True)),
                ('isMissing', models.BooleanField(default=0, help_text='year since le bac', null=True, verbose_name='year')),
                ('date', models.DateField(default='0000-00001', max_length=9, null=True)),
                ('student', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='lycee.Student')),
            ],
        ),
    ]
