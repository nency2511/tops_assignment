# Generated by Django 4.2.4 on 2024-04-04 11:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_api', '0002_author_book'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='pname',
            new_name='book_name',
        ),
        migrations.AlterField(
            model_name='book',
            name='author_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_api.author'),
        ),
    ]
