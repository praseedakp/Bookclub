# Generated by Django 4.2.3 on 2023-07-29 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='regmodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uname', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('psw', models.CharField(max_length=50)),
            ],
        ),
    ]
