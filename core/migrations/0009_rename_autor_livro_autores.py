# Generated by Django 5.1.1 on 2024-10-31 00:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0008_livro"),
    ]

    operations = [
        migrations.RenameField(
            model_name="livro",
            old_name="autor",
            new_name="autores",
        ),
    ]
