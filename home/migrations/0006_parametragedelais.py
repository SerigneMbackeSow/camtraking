# Generated by Django 4.2.9 on 2024-07-15 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_mouvement2'),
    ]

    operations = [
        migrations.CreateModel(
            name='ParametrageDelais',
            fields=[
                ('id_para', models.AutoField(db_column='id_chauffeur', primary_key=True, serialize=False)),
                ('entite', models.CharField(max_length=255)),
                ('nbr_max', models.CharField(max_length=255, null=True)),
                ('type', models.CharField(max_length=20)),
                ('duree', models.CharField(max_length=20)),
            ],
        ),
    ]
