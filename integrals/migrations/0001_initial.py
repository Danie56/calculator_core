# Generated by Django 5.0.6 on 2024-05-17 03:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Integral',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_method', models.CharField(max_length=200)),
                ('expression', models.CharField(max_length=200)),
                ('sub_intervals', models.IntegerField(default=0)),
                ('result', models.FloatField(default=None, null=True)),
            ],
        ),
    ]
