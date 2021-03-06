# Generated by Django 2.0.13 on 2019-05-27 19:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField()),
                ('activity', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Mood',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField()),
                ('mood_entry', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('userid', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='mood',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.User'),
        ),
        migrations.AddField(
            model_name='activity',
            name='mood',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.Mood'),
        ),
        migrations.AddField(
            model_name='activity',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.User'),
        ),
    ]
