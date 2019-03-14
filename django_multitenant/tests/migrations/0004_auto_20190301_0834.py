# Generated by Django 2.1.1 on 2019-03-01 08:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tests', '0003_auto_20181220_1151'),
    ]

    operations = [
        migrations.AlterField(
            model_name='manager',
            name='account',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='managers', to='tests.Account'),
        ),
        migrations.AlterField(
            model_name='project',
            name='account',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='projects', to='tests.Account'),
        ),
    ]