# Generated by Django 4.1.5 on 2023-01-07 14:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_alter_orders_items_item'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders_items',
            name='item',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.items'),
        ),
    ]
