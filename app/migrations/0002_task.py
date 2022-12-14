# Generated by Django 4.0.6 on 2022-08-01 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=100)),
                ('description', models.TextField(default='')),
                ('file', models.FileField(default='', upload_to='files/')),
                ('client_amount', models.IntegerField(default=0)),
                ('admin_amount', models.IntegerField(default=0)),
                ('due_date', models.DateField(default='')),
                ('status', models.CharField(default='', max_length=100)),
            ],
        ),
    ]
