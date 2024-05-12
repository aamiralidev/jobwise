# Generated by Django 4.2.2 on 2024-05-12 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='board_url',
            field=models.CharField(default='https://boards.greenhouse.io', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='job',
            name='open',
            field=models.BooleanField(default=True),
        ),
    ]