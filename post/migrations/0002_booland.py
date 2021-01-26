# Generated by Django 3.1.5 on 2021-01-07 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booland',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='название')),
                ('description', models.TextField(verbose_name='описание')),
                ('booled', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'это',
                'verbose_name_plural': 'Эти',
            },
        ),
    ]
