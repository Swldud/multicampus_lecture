# Generated by Django 3.2.18 on 2023-03-28 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('balance', models.IntegerField()),
                ('major', models.CharField(max_length=10)),
                ('phone', models.CharField(max_length=20)),
                ('mbti', models.CharField(max_length=4)),
                ('address', models.CharField(max_length=100)),
            ],
        ),
    ]
