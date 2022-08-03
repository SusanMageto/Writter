# Generated by Django 4.0.6 on 2022-08-01 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_task'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='admin_amount',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='client_amount',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='description',
            field=models.TextField(blank=True, default='', null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='due_date',
            field=models.DateField(blank=True, default='', null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='file',
            field=models.FileField(default='', null=True, upload_to='files/'),
        ),
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.CharField(blank=True, default='', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='title',
            field=models.CharField(blank=True, default='', max_length=100, null=True),
        ),
    ]
