# Generated by Django 4.1.2 on 2022-11-05 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0003_remove_todo_todo_order_todo_todo_current_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todo',
            name='todo_current',
        ),
        migrations.AlterField(
            model_name='todo',
            name='todo_id',
            field=models.AutoField(primary_key=True, serialize=False, unique=True),
        ),
    ]
