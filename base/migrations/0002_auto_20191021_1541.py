# Generated by Django 2.2.6 on 2019-10-21 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='membership',
            name='skill_level',
            field=models.CharField(choices=[('None', 'Choose level...'), ('Beginner', 'Beginner'), ('Intermediate', 'Intermediate'), ('Advanced', 'Advanced')], max_length=3),
        ),
    ]
