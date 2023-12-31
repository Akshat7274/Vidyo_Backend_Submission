# Generated by Django 4.2.7 on 2023-11-12 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ExtractAudio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30)),
                ('input', models.CharField(max_length=500)),
                ('output', models.CharField(max_length=500)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Watermark',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30)),
                ('video', models.CharField(max_length=500)),
                ('image', models.CharField(max_length=500)),
                ('output', models.CharField(max_length=500)),
                ('size', models.CharField(max_length=15)),
                ('position', models.CharField(max_length=15)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
