# Generated by Django 3.2.9 on 2021-12-20 08:46

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('sim_manager', '0005_auto_20211215_1554'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Access',
            new_name='Share',
        ),
        migrations.RenameField(
            model_name='share',
            old_name='user',
            new_name='user_share',
        ),
        migrations.AddConstraint(
            model_name='favorite',
            constraint=models.UniqueConstraint(fields=('user', 'simulation'), name="Une simulation ne peut être mise qu'une fois en favori par un utilisateur"),
        ),
        migrations.AddConstraint(
            model_name='share',
            constraint=models.UniqueConstraint(fields=('simulation', 'user_share'), name='Une simulation ne peut pas être partagée 2 fois avec le même utilisateur'),
        ),
    ]