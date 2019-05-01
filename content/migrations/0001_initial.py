# Generated by Django 2.2 on 2019-05-01 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Iris',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sepal_length', models.DecimalField(decimal_places=1, max_digits=2)),
                ('sepal_width', models.DecimalField(decimal_places=1, max_digits=2)),
                ('petal_length', models.DecimalField(decimal_places=1, max_digits=2)),
                ('petal_width', models.DecimalField(decimal_places=1, max_digits=2)),
                ('CLASS', models.CharField(choices=[('SE', 'SETOSA'), ('VE', 'VERSICOLOUR'), ('VI', 'VIRGINICA')], max_length=11)),
            ],
        ),
    ]