# Generated by Django 4.1.1 on 2022-09-08 21:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0006_alter_post_body'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='snippet',
            field=models.CharField(default='This is a intro', max_length=255),
        ),
    ]
