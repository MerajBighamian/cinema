# Generated by Django 3.0.10 on 2020-09-19 12:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20200918_2017'),
        ('ticketing', '0005_auto_20200918_1811'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seat_count', models.IntegerField(verbose_name='تعداد صندلی')),
                ('order_time', models.DateTimeField(auto_now_add=True, verbose_name='زمان خرید')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='accounts.Profile', verbose_name='کاربر')),
                ('showtime', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='ticketing.ShowTime', verbose_name='سانس')),
            ],
            options={
                'verbose_name': 'بلیت',
                'verbose_name_plural': 'ها',
            },
        ),
    ]
