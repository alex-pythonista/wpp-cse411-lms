# Generated by Django 3.1.6 on 2021-03-30 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_auto_20210330_0831'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='product',
            new_name='book',
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Issued', 'Issued'), ('Returned', 'Returned'), ('Late Submission', 'Late Submission')], max_length=200, null=True),
        ),
    ]
