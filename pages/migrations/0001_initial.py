# Generated by Django 4.2.1 on 2023-09-08 11:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='My_result',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('years_experience', models.IntegerField(default=0)),
                ('expert_technicians', models.IntegerField(default=0)),
                ('satisfied_clients', models.IntegerField(default=0)),
                ('compleate_Projects', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Our_expert',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('facebook', models.URLField(max_length=50)),
                ('instagram', models.URLField(max_length=50)),
                ('img', models.ImageField(upload_to='images/')),
                ('profeccion', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Our_services',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('services_name', models.CharField(max_length=200)),
                ('services_about', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Work_time',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=30)),
                ('ish_vaqti', models.DateTimeField()),
                ('phone_number', models.CharField(max_length=15)),
                ('facebook', models.URLField(max_length=50)),
                ('instagram', models.URLField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Our_clients',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_name', models.CharField(max_length=15)),
                ('massage', models.CharField(max_length=100)),
                ('client_services', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pages.our_services')),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=20)),
                ('services_date', models.DateField()),
                ('bio', models.CharField(max_length=30)),
                ('services_namee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pages.our_services')),
            ],
        ),
    ]
