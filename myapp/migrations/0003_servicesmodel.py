# Generated by Django 4.2.10 on 2024-03-13 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_patientmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='servicesmodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('serviceimage', models.ImageField(upload_to='images/')),
            ],
        ),
    ]