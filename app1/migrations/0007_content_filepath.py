# Generated by Django 3.2.9 on 2021-12-20 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0006_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='content',
            name='filepath',
            field=models.FileField(null=True, upload_to='', verbose_name=''),
        ),
    ]