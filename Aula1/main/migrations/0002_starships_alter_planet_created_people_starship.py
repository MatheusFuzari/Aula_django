# Generated by Django 4.2.4 on 2023-08-03 01:55

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Starships',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('model', models.CharField(max_length=20)),
                ('passengers', models.IntegerField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('length', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.AlterField(
            model_name='planet',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 3, 1, 55, 52, 403023, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AddField(
            model_name='people',
            name='starship',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='starship', to='main.starships'),
        ),
    ]
