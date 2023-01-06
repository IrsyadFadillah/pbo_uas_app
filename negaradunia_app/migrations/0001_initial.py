# Generated by Django 4.1.1 on 2022-10-31 09:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Benua",
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
                ("nama_benua", models.CharField(max_length=20)),
                ("keterangan", models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name="Negara",
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
                ("nama_negara", models.CharField(max_length=50)),
                ("letak_astronomi", models.CharField(max_length=40)),
                ("ibu_kota", models.CharField(max_length=40)),
                ("mata_uang", models.CharField(max_length=40)),
                ("bahasa_resmi", models.CharField(max_length=40)),
                ("bentuk_pemerintahan", models.CharField(max_length=70)),
                (
                    "benua_id",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="negaradunia_app.benua",
                    ),
                ),
            ],
        ),
    ]
