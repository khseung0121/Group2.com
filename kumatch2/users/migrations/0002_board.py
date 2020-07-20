# Generated by Django 3.0.8 on 2020-07-17 04:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Board',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('b_title', models.CharField(max_length=126, verbose_name='제목')),
                ('b_note', models.TextField(verbose_name='내용')),
                ('b_writer', models.CharField(max_length=16, verbose_name='작성자')),
                ('b_date', models.DateTimeField(auto_now_add=True, verbose_name='작성일')),
            ],
        ),
    ]