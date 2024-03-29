# Generated by Django 4.1.12 on 2024-01-10 00:18

import cloudinary.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cities',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'cities',
            },
        ),
        migrations.CreateModel(
            name='States',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'states',
            },
        ),
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=255)),
                ('address', models.CharField(default='', max_length=255)),
                ('rating', models.DecimalField(decimal_places=2, default=0.0, max_digits=3)),
                ('charges', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('city', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='apis.cities')),
                ('state', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='apis.states')),
            ],
            options={
                'db_table': 'vendors',
            },
        ),
        migrations.CreateModel(
            name='VendorTypes',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'vendor_types',
            },
        ),
        migrations.CreateModel(
            name='Venue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=255)),
                ('address', models.CharField(default='', max_length=255)),
                ('rating', models.DecimalField(decimal_places=2, default=0.0, max_digits=3)),
                ('capacity', models.PositiveIntegerField(default=0)),
                ('city', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='apis.cities')),
                ('state', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='apis.states')),
            ],
            options={
                'db_table': 'venues',
            },
        ),
        migrations.CreateModel(
            name='VenueTypes',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('type', models.CharField(blank=True, default=None, max_length=255, null=True)),
            ],
            options={
                'db_table': 'venue_types',
            },
        ),
        migrations.CreateModel(
            name='VenueLogin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='', max_length=255)),
                ('email', models.EmailField(blank=True, default='', max_length=254)),
                ('phone_number', models.CharField(blank=True, default='', max_length=20)),
                ('user_name', models.CharField(default='', max_length=255, unique=True)),
                ('password', models.CharField(default='', max_length=255)),
                ('city', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='apis.cities')),
                ('venue_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='apis.venuetypes')),
            ],
            options={
                'db_table': 'venue_logins',
            },
        ),
        migrations.CreateModel(
            name='VenueImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', cloudinary.models.CloudinaryField(max_length=255, verbose_name='image')),
                ('venue', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='venue_images', to='apis.venue')),
            ],
            options={
                'db_table': 'venue_images',
            },
        ),
        migrations.AddField(
            model_name='venue',
            name='venue_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='venues', to='apis.venuetypes'),
        ),
        migrations.CreateModel(
            name='VendorLogin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='', max_length=255)),
                ('email', models.EmailField(blank=True, default='', max_length=254)),
                ('phone_number', models.CharField(blank=True, default='', max_length=20)),
                ('user_name', models.CharField(default='', max_length=255, unique=True)),
                ('password', models.CharField(default='', max_length=255)),
                ('city', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='apis.cities')),
                ('vendor_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='apis.vendortypes')),
            ],
            options={
                'db_table': 'vendor_logins',
            },
        ),
        migrations.CreateModel(
            name='VendorImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', cloudinary.models.CloudinaryField(max_length=255, verbose_name='image')),
                ('vendor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vendor_images', to='apis.vendor')),
            ],
            options={
                'db_table': 'vendor_images',
            },
        ),
        migrations.AddField(
            model_name='vendor',
            name='vendor_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='vendors', to='apis.vendortypes'),
        ),
        migrations.CreateModel(
            name='UserLogin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='', max_length=255)),
                ('email', models.EmailField(blank=True, default='', max_length=254)),
                ('password', models.CharField(default='', max_length=255)),
                ('date', models.DateField(blank=True, null=True)),
                ('event_city', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='apis.cities')),
            ],
            options={
                'db_table': 'user_logins',
            },
        ),
        migrations.AddField(
            model_name='cities',
            name='state',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='cities', to='apis.states'),
        ),
    ]
