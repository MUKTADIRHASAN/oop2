# Generated by Django 5.0.4 on 2024-05-02 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_post_content_tag'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='Main_post',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='post',
            name='section',
            field=models.CharField(choices=[('Main_post', 'Main_post'), ('Popular', 'Popular'), ('Recent', 'Recent'), ('Editors_Pick', 'Editors_Pick'), ('Trending', 'Trending'), ('Inspiration', 'Inspiration'), ('Latest Post', 'Latest Post')], max_length=200),
        ),
    ]
