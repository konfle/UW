# Generated by Django 3.1.1 on 2020-09-28 13:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('uwapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='posttraining',
            old_name='published_date',
            new_name='data_opublikowania',
        ),
    ]