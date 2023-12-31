# Generated by Django 4.2.3 on 2023-07-30 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='bookmodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bookna', models.CharField(max_length=60)),
                ('bookau', models.CharField(max_length=50)),
                ('bookpdf', models.FileField(upload_to='book_app/static')),
                ('bookimage', models.FileField(upload_to='book_app/static')),
                ('date', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
