# Generated by Django 4.1.4 on 2023-01-09 09:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('transaction', '0002_alter_journal_transaction'),
    ]

    operations = [
        migrations.AlterField(
            model_name='journal',
            name='transaction',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='transaction.transaction'),
        ),
    ]
