# Generated by Django 2.2.10 on 2021-12-02 04:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='polls',
            field=models.ManyToManyField(related_name='to_polls', to='polls.Poll'),
        ),
    ]
