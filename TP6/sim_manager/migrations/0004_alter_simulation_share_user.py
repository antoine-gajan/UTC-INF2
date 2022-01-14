# Generated by Django 3.2.9 on 2021-12-14 16:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('sim_manager', '0003_auto_20211213_0945'),
    ]

    operations = [
        migrations.AlterField(
            model_name='simulation',
            name='share_user',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='share_user', to=settings.AUTH_USER_MODEL),
        ),
    ]