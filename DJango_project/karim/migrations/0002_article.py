# Generated by Django 3.0.3 on 2020-05-10 00:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('karim', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20000)),
                ('link', models.CharField(max_length=1000)),
                ('tag', models.CharField(max_length=1000)),
                ('source', models.CharField(max_length=1000)),
            ],
        ),
    ]
