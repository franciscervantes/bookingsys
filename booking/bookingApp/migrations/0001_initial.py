# Generated by Django 3.0.8 on 2020-08-01 09:26

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
                ('username', models.CharField(max_length=128)),
                ('password', models.CharField(max_length=128)),
            ],
            options={
                'db_table': 'admin',
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
                ('room_type_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='bookingApp.RoomType')),
            ],
            options={
                'db_table': 'room',
            },
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('reservation_id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=128)),
                ('last_name', models.CharField(max_length=128)),
                ('client_email', models.CharField(max_length=128)),
                ('client_phone', models.CharField(max_length=128)),
                ('date_in', models.DateField()),
                ('date_out', models.DateField()),
                ('room_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='bookingApp.Room')),
            ],
            options={
                'db_table': 'reservation',
            },
        ),
    ]
