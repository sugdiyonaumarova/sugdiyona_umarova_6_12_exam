# Generated by Django 5.0.6 on 2024-06-04 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='attribute',
            field=models.ManyToManyField(blank=True, null=True, to='blog.attribute'),
        ),
        migrations.DeleteModel(
            name='ProductAttribute',
        ),
    ]
