# Generated by Django 4.0.3 on 2022-04-09 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0008_alter_sample_u_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='mobile',
            field=models.CharField(blank=True, max_length=12, null=True),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to='profiles/'),
        ),
    ]
