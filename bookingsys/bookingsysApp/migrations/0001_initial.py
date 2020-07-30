# Generated by Django 3.0.8 on 2020-07-28 07:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('admin_id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=128)),
                ('last_name', models.CharField(max_length=128)),
                ('admin_email', models.CharField(max_length=128)),
            ],
            options={
                'db_table': 'admin',
            },
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('client_id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=128)),
                ('last_name', models.CharField(max_length=128)),
                ('client_address', models.CharField(max_length=255)),
                ('client_email', models.CharField(max_length=128)),
                ('city', models.CharField(max_length=65)),
                ('country', models.CharField(max_length=65)),
                ('client_phone_num', models.CharField(max_length=65)),
            ],
            options={
                'db_table': 'client',
            },
        ),
        migrations.CreateModel(
            name='RoomType',
            fields=[
                ('room_type_id', models.AutoField(primary_key=True, serialize=False)),
                ('type_name', models.CharField(max_length=64)),
                ('price', models.IntegerField()),
            ],
            options={
                'db_table': 'room_type',
            },
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('room_id', models.AutoField(primary_key=True, serialize=False)),
                ('room_status', models.CharField(max_length=128)),
                ('room_num', models.IntegerField(blank=True, null=True)),
                ('room_type_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookingsysApp.RoomType')),
            ],
            options={
                'db_table': 'room',
            },
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('reservation_id', models.AutoField(primary_key=True, serialize=False)),
                ('date_in', models.DateField()),
                ('date_out', models.DateField()),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookingsysApp.Client')),
                ('room_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookingsysApp.Room')),
            ],
            options={
                'db_table': 'reservation',
            },
        ),
        migrations.CreateModel(
            name='PaymentDetails',
            fields=[
                ('payment_details_id', models.AutoField(primary_key=True, serialize=False)),
                ('value', models.IntegerField()),
                ('days', models.IntegerField()),
                ('total', models.IntegerField()),
                ('reservation_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookingsysApp.Reservation')),
            ],
            options={
                'db_table': 'payment_details',
            },
        ),
    ]
