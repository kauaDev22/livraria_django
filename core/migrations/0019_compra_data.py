# Generated by Django 5.1.3 on 2024-12-18 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0018_remove_compra_data'),
    ]

    operations = [
        migrations.AddField(
            model_name='compra',
            name='data',
            field=models.DateTimeField(auto_now_add=True, default='2024-10-01 15:08:00'),
            preserve_default=False,
        ),
    ]
