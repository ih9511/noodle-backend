# Generated by Django 5.1.1 on 2024-09-25 10:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('branches', '0002_rename_branchname_branches_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Commits',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('message', models.TextField()),
                ('author', models.CharField(max_length=32)),
                ('time', models.DateTimeField()),
                ('branch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='branches.branches')),
            ],
            options={
                'db_table': 'commits',
            },
        ),
    ]
