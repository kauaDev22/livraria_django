# Generated by Django 5.1.2 on 2024-11-04 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_livro_categoria_livro_editora'),
    ]

    operations = [
        migrations.AddField(
            model_name='livro',
            name='autores',
            field=models.ManyToManyField(blank=True, related_name='Livros', to='core.autor'),
        ),
    ]
