# Generated by Django 2.2.4 on 2023-06-11 08:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_one', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=45)),
                ('description', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('uploded_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='books', to='app_one.User')),
                ('users_who_like', models.ManyToManyField(related_name='liked_books', to='app_one.User')),
            ],
        ),
    ]