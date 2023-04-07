# Generated by Django 4.1.7 on 2023-04-04 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_order'),
    ]

    operations = [
        migrations.CreateModel(
            name='MenuItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('description', models.TextField()),
            ],
        ),
        migrations.RenameField(
            model_name='order',
            old_name='date_created',
            new_name='created_at',
        ),
        migrations.RemoveField(
            model_name='order',
            name='customer_address',
        ),
        migrations.RemoveField(
            model_name='order',
            name='customer_name',
        ),
        migrations.RemoveField(
            model_name='order',
            name='customer_phone',
        ),
        migrations.AlterField(
            model_name='order',
            name='items',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='order',
            name='total_price',
            field=models.DecimalField(decimal_places=2, max_digits=6),
        ),
    ]