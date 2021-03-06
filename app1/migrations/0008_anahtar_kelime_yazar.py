# Generated by Django 3.2.9 on 2021-12-21 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0007_content_filepath'),
    ]

    operations = [
        migrations.CreateModel(
            name='anahtar_kelime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('anahtar_kelime', models.CharField(max_length=50)),
                ('filepath', models.CharField(max_length=50)),
                ('file_id', models.CharField(max_length=50)),
                ('kullanıcı_id', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='yazar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('yazar_ad', models.CharField(max_length=50)),
                ('yazar_soyad', models.CharField(max_length=50)),
                ('öğrenci_numarası', models.CharField(max_length=50)),
                ('öğretim_türü', models.CharField(max_length=50)),
                ('filepath', models.CharField(max_length=50)),
                ('file_id', models.CharField(max_length=50)),
                ('kullanıcı_id', models.CharField(max_length=50)),
            ],
        ),
    ]
