# Generated by Django 4.0 on 2021-12-30 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Studentapp', '0002_alter_register_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='dashboard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('image', models.ImageField(default='', upload_to='media')),
            ],
            options={
                'db_table': 'dashdb',
            },
        ),
    ]
