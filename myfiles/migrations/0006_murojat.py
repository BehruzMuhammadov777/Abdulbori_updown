# Generated by Django 4.0.4 on 2022-10-14 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myfiles', '0005_clients_lavozimi'),
    ]

    operations = [
        migrations.CreateModel(
            name='Murojat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('mail', models.CharField(max_length=800)),
                ('subject', models.CharField(max_length=800)),
                ('messege', models.TextField()),
                ('vaqt', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
