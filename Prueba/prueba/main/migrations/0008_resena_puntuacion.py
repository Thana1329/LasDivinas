# Generated by Django 4.2.4 on 2023-10-23 23:23

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0007_resena_delete_registrousuario_remove_productos_slug_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="resena",
            name="puntuacion",
            field=models.PositiveIntegerField(default=0),
        ),
    ]
