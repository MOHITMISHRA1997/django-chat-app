# Generated by Django 4.2.6 on 2023-10-28 07:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('myapp', '0006_rename_status_onlineuser_is_online'),
    ]

    operations = [
        migrations.CreateModel(
            name='Userprofile',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('profile_img', models.ImageField(upload_to='users_dp/')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
