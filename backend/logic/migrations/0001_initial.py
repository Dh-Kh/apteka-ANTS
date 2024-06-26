# Generated by Django 4.2.8 on 2024-05-03 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EmployeeModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('path', models.CharField(max_length=255, unique=True)),
                ('depth', models.PositiveIntegerField()),
                ('numchild', models.PositiveIntegerField(default=0)),
                ('full_name', models.CharField(max_length=255)),
                ('position', models.IntegerField(choices=[(7, 'SEO'), (6, 'Team Lead'), (5, 'Tech Lead'), (4, 'Senior'), (3, 'Middle'), (2, 'Junior'), (1, 'Trainee')])),
                ('joined', models.DateField()),
                ('email', models.EmailField(max_length=254)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
