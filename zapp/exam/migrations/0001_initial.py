# Generated by Django 4.1.5 on 2023-04-15 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exam_name', models.CharField(max_length=101)),
                ('exam_type', models.CharField(max_length=101)),
                ('exam_time', models.CharField(max_length=101)),
                ('exam_date', models.CharField(max_length=101)),
                ('exam_marks', models.CharField(max_length=101)),
            ],
        ),
    ]