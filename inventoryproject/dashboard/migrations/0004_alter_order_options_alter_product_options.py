# Generated by Django 4.1.1 on 2022-09-10 22:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("dashboard", "0003_order"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="order", options={"verbose_name_plural": "Order"},
        ),
        migrations.AlterModelOptions(
            name="product", options={"verbose_name_plural": "Product"},
        ),
    ]