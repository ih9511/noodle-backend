# Generated by Django 5.1.1 on 2024-09-30 08:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("backlog", "0002_alter_backlog_id"),
    ]

    operations = [
        migrations.CreateModel(
            name="BacklogIssue",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("issue", models.CharField(max_length=500)),
                (
                    "backlog",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="issues",
                        to="backlog.backlog",
                    ),
                ),
            ],
            options={
                "db_table": "backlog_issue",
            },
        ),
    ]
