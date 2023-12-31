# Generated by Django 4.2.6 on 2023-10-13 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flights', '0005_alter_airport_city_alter_airport_code'),
    ]

    operations = [
        migrations.CreateModel(
            name='Passenger',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first', models.CharField(max_length=64)),
                ('last', models.CharField(max_length=64)),
                ('flights', models.ManyToManyField(blank=True, related_name='passengers', to='flights.flight')),
            ],
        ),
    ]
