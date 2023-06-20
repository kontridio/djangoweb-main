# Generated by Django 4.2 on 2023-06-20 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('utulek', '0009_remove_mesto_psc'),
    ]

    operations = [
        migrations.AddField(
            model_name='pes',
            name='pohlavi',
            field=models.CharField(choices=[('PES', 'Pes'), ('FENA', 'Fena')], default=0, max_length=4, verbose_name='Pohlaví'),
        ),
    ]
