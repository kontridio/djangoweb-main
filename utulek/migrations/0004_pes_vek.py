# Generated by Django 4.2 on 2023-06-20 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('utulek', '0003_pes_fotografie_alter_mesto_nazev_mesta'),
    ]

    operations = [
        migrations.AddField(
            model_name='pes',
            name='vek',
            field=models.PositiveSmallIntegerField(default=1, verbose_name='Věk'),
            preserve_default=False,
        ),
    ]