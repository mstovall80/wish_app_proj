# Generated by Django 2.2.4 on 2021-03-04 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wish_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Wish',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('wish', models.CharField(max_length=200)),
                ('like', models.IntegerField()),
            ],
        ),
    ]