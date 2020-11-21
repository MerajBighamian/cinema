# Generated by Django 3.0.7 on 2020-08-09 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticketing', '0003_auto_20200701_1109'),
    ]

    operations = [
        migrations.AddField(
            model_name='cinema',
            name='poster',
            field=models.ImageField(null=True, upload_to='imageposter/', verbose_name='پوستر'),
        ),
        migrations.AddField(
            model_name='movie',
            name='poster',
            field=models.ImageField(default='temporary', upload_to='imageposter/', verbose_name='پوستر'),
            preserve_default=False,
        ),
    ]