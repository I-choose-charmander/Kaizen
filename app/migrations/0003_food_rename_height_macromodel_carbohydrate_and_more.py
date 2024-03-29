# Generated by Django 5.0.2 on 2024-03-23 23:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_macromodel_delete_stockdata'),
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('food', models.CharField(max_length=50)),
            ],
        ),
        migrations.RenameField(
            model_name='macromodel',
            old_name='height',
            new_name='carbohydrate',
        ),
        migrations.AddField(
            model_name='macromodel',
            name='fat',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='macromodel',
            name='protien',
            field=models.IntegerField(default=0),
        ),
    ]
