# Generated by Django 4.2.5 on 2023-10-02 00:18

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("storage", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="product",
            name="price",
        ),
    ]
