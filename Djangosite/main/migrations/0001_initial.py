# Generated by Django 5.0.4 on 2024-04-19 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullName', models.CharField(max_length=255)),
                ('about', models.TextField()),
                ('timeUpdate', models.DateField(auto_now_add=True)),
                ('photo', models.ImageField(upload_to='photos/')),
            ],
        ),
    ]