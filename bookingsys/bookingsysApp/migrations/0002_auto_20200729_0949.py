# Generated by Django 3.0.8 on 2020-07-29 01:49

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('bookingsysApp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='city',
        ),
        migrations.RemoveField(
            model_name='client',
            name='client_address',
        ),
        migrations.RemoveField(
            model_name='client',
            name='client_phone_num',
        ),
        migrations.RemoveField(
            model_name='client',
            name='country',
        ),
        migrations.AddField(
            model_name='client',
            name='client_image',
            field=models.CharField(default=django.utils.timezone.now, max_length=256),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='client',
            name='google_id',
            field=models.CharField(default=django.utils.timezone.now, max_length=256),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='paymentdetails',
            name='reservation_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='bookingsysApp.Reservation'),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='bookingsysApp.Client'),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='room_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='bookingsysApp.Room'),
        ),
        migrations.AlterField(
            model_name='room',
            name='room_type_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='bookingsysApp.RoomType'),
        ),
    ]