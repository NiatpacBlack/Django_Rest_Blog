# Generated by Django 4.1.1 on 2022-10-03 20:10

from django.db import migrations
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ("taggit", "0005_auto_20220424_2025"),
        ("blog_app", "0008_alter_postmodel_author_alter_postmodel_content_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="postmodel",
            name="tag",
            field=taggit.managers.TaggableManager(
                blank=True,
                help_text="A comma-separated list of tags.",
                through="taggit.TaggedItem",
                to="taggit.Tag",
                verbose_name="Теги",
            ),
        ),
    ]