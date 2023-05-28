# Generated by Django 4.2 on 2023-05-28 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0002_alter_booking_id_alter_menu_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='booking_date',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='booking',
            name='id',
            field=models.PositiveIntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='menu',
            name='id',
            field=models.PositiveIntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='menu',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
        migrations.AlterField(
            model_name='menu',
            name='title',
            field=models.CharField(max_length=255),
        ),
    ]