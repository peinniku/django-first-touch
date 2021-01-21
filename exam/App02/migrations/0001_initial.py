# Generated by Django 2.2 on 2020-07-11 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('regtime', models.DateTimeField(auto_created=True)),
                ('uid', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=30, unique=True)),
                ('password', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'user',
                'ordering': ['-regtime'],
            },
        ),
    ]