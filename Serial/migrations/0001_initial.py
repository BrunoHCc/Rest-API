# Generated by Django 4.1.7 on 2023-02-14 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='leite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=20)),
                ('temp', models.CharField(max_length=4)),
                ('volume', models.CharField(max_length=8)),
            ],
        ),
    ]
