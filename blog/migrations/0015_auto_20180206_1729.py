# Generated by Django 2.0 on 2018-02-06 09:29

import blog.files_handle
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_auto_20180203_2211'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postmodel',
            name='image',
            field=blog.files_handle.ThumbnailImageField(upload_to='./article/'),
        ),
    ]
