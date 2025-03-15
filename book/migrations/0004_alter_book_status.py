# Generated by Django 5.1.7 on 2025-03-15 00:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0003_alter_book_isbn'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='status',
            field=models.CharField(choices=[('available', 'disponível'), ('on_loan', 'emprestado')], default=('available', 'disponível'), max_length=10),
        ),
    ]
