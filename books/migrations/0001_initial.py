# Generated by Django 4.0.1 on 2022-01-12 20:33

import autoslug.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0002_alter_user_id'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=240)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='title', unique=True)),
                ('lead_text', models.CharField(default='', max_length=254)),
                ('view_count', models.IntegerField(blank=True, default=0)),
                ('featured', models.BooleanField(blank=True, default=False)),
                ('price', models.DecimalField(blank=True, decimal_places=2, default='0.00', max_digits=5, null=True)),
                ('avg_rate', models.DecimalField(decimal_places=2, default=None, max_digits=5, null=True)),
                ('an_likes', models.IntegerField(default=None, null=True)),
                ('max_rating', models.DecimalField(decimal_places=2, default=None, max_digits=5, null=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='books', to='books.author')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='UserBookRelation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('like', models.BooleanField(blank=True, default=False)),
                ('dislike', models.BooleanField(blank=True, default=False)),
                ('in_bookmark', models.BooleanField(blank=True, default=False)),
                ('rating', models.PositiveSmallIntegerField(blank=True, choices=[(1, 'OK'), (2, 'Fine'), (3, 'Good'), (4, 'Amazing'), (5, 'Excellent')], null=True)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.book')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='fans',
            field=models.ManyToManyField(related_name='book_fans', through='books.UserBookRelation', to=settings.AUTH_USER_MODEL),
        ),
    ]
