# Generated by Django 3.0.4 on 2020-08-31 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40)),
                ('pub_date', models.DateField()),
                ('body', models.CharField(max_length=1000)),
                ('image', models.ImageField(upload_to='images/')),
            ],
        ),
    ]