# Generated by Django 4.0.4 on 2022-06-03 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MiniNewsApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogs',
            name='Blog_Description',
            field=models.TextField(default='0', max_length=350),
        ),
        migrations.AlterField(
            model_name='blogs',
            name='Blog_Tittle',
            field=models.CharField(default='0', max_length=50),
        ),
    ]
