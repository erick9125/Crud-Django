# Generated by Django 2.1.2 on 2018-11-05 04:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice_text', models.CharField(max_length=200)),
                ('votes', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Mascota',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank='true', max_length=200)),
                ('raza', models.CharField(max_length=15)),
                ('Descripcion', models.CharField(max_length=200)),
                ('Estado', models.CharField(max_length=200)),
                ('image', models.FileField(blank='true', upload_to='images')),
            ],
            options={
                'db_table': 'mascota_question',
            },
        ),
        migrations.AddField(
            model_name='choice',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mascota.Mascota'),
        ),
    ]
