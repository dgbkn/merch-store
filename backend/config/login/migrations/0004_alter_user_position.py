# Generated by Django 4.1.4 on 2023-06-15 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("login", "0003_user_name_user_phone_no_user_position"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="position",
            field=models.CharField(
                choices=[
                    ("MB", "Member"),
                    ("CR", "Core"),
                    ("JS", "Joint Secretary"),
                    ("FS", "Finance Secretary"),
                    ("GS", "General Secretary"),
                ],
                default="MB",
                max_length=2,
            ),
        ),
    ]