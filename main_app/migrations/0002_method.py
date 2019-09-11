# Generated by Django 2.2.3 on 2019-09-11 18:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Method',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('methods', models.CharField(choices=[('E', 'espresso machine'), ('A', 'aeropress'), ('P', 'pour over'), ('M', 'manual coffee machine'), ('F', 'french press')], default='espresso machine', max_length=1)),
                ('coffee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.Coffee')),
            ],
        ),
    ]
