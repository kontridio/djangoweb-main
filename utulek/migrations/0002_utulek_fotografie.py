# Generated by Django 4.2 on 2023-06-18 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('utulek', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='utulek',
            name='fotografie',
            field=models.ImageField(blank=True, null=True, upload_to='utulky', verbose_name='Fotografie'),
        ),
    ]