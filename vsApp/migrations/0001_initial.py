# Generated by Django 4.0.3 on 2022-03-12 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('ratings', models.DecimalField(decimal_places=2, max_digits=4)),
            ],
        ),
    ]
