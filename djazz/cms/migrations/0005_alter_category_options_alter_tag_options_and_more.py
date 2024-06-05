# Generated by Django 5.0.6 on 2024-05-10 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0004_alter_post_seo_keywords_alter_post_seo_title'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ('title',), 'verbose_name': 'category', 'verbose_name_plural': 'categories'},
        ),
        migrations.AlterModelOptions(
            name='tag',
            options={'ordering': ('title',), 'verbose_name': 'tag', 'verbose_name_plural': 'tags'},
        ),
        migrations.RenameField(
            model_name='category',
            old_name='name',
            new_name='title',
        ),
        migrations.RenameField(
            model_name='tag',
            old_name='name',
            new_name='title',
        ),
        migrations.RemoveField(
            model_name='category',
            name='seo_description',
        ),
        migrations.RemoveField(
            model_name='category',
            name='seo_keywords',
        ),
        migrations.RemoveField(
            model_name='category',
            name='seo_title',
        ),
        migrations.RemoveField(
            model_name='page',
            name='seo_description',
        ),
        migrations.RemoveField(
            model_name='page',
            name='seo_keywords',
        ),
        migrations.RemoveField(
            model_name='page',
            name='seo_title',
        ),
        migrations.RemoveField(
            model_name='post',
            name='seo_description',
        ),
        migrations.RemoveField(
            model_name='post',
            name='seo_keywords',
        ),
        migrations.RemoveField(
            model_name='post',
            name='seo_title',
        ),
        migrations.RemoveField(
            model_name='tag',
            name='seo_description',
        ),
        migrations.RemoveField(
            model_name='tag',
            name='seo_keywords',
        ),
        migrations.RemoveField(
            model_name='tag',
            name='seo_title',
        ),
        migrations.AddField(
            model_name='category',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='category',
            name='keywords',
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.AddField(
            model_name='page',
            name='description',
            field=models.TextField(blank=True, max_length=250),
        ),
        migrations.AddField(
            model_name='page',
            name='keywords',
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.AddField(
            model_name='post',
            name='description',
            field=models.TextField(blank=True, max_length=250),
        ),
        migrations.AddField(
            model_name='post',
            name='keywords',
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.AddField(
            model_name='tag',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='tag',
            name='keywords',
            field=models.CharField(blank=True, max_length=250),
        ),
    ]