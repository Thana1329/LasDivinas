# Generated by Django 4.2.4 on 2023-10-19 18:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0006_categoria_description"),
    ]

    operations = [
        migrations.CreateModel(
            name="Resena",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("comentario", models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name="registroUsuario",
        ),
        migrations.RemoveField(
            model_name="productos",
            name="slug",
        ),
        migrations.AddField(
            model_name="resena",
            name="producto",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="main.productos"
            ),
        ),
    ]
