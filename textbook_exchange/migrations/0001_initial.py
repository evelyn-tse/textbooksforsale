# Generated by Django 4.1.2 on 2022-12-06 23:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Book",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=100)),
                ("ISBN", models.IntegerField()),
                ("author", models.CharField(max_length=50)),
                ("price", models.IntegerField()),
                ("condition", models.CharField(default="Good", max_length=10)),
                ("course", models.CharField(default="CS 3240", max_length=20)),
                ("instructor", models.CharField(default="none", max_length=50)),
                ("seller", models.CharField(default="evelyn8", max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name="Course",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("subject", models.CharField(max_length=10)),
                ("catalog_number", models.CharField(max_length=14)),
                ("instructor", models.CharField(default="Unknown", max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name="Department",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("subject", models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name="Instructor",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("instructor", models.CharField(max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name="Profile",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=20, null=True)),
                ("year", models.IntegerField(null=True)),
                ("email", models.CharField(max_length=15, null=True)),
                (
                    "user",
                    models.OneToOneField(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="FriendsList",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "friends",
                    models.ManyToManyField(
                        blank=True, related_name="friends", to=settings.AUTH_USER_MODEL
                    ),
                ),
                (
                    "user",
                    models.OneToOneField(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="FriendRequest",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("sender_confirm", models.BooleanField(default=False)),
                ("receiver_confirm", models.BooleanField(default=False)),
                (
                    "receiver",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="receiver",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "sender",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="sender",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="FavoriteBooks",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "books",
                    models.ManyToManyField(
                        blank=True, related_name="books", to="textbook_exchange.book"
                    ),
                ),
                (
                    "user",
                    models.OneToOneField(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Class",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("instructor", models.CharField(max_length=80)),
                ("instructor_email", models.CharField(max_length=80)),
                ("course_number", models.IntegerField()),
                ("semester_code", models.IntegerField()),
                ("course_section", models.IntegerField()),
                ("subject", models.CharField(max_length=10)),
                ("catalog_number", models.IntegerField()),
                ("description", models.CharField(max_length=100)),
                ("units", models.CharField(max_length=10)),
                ("component", models.CharField(max_length=10)),
                ("class_capacity", models.IntegerField()),
                ("wait_list", models.IntegerField()),
                ("wait_cap", models.IntegerField()),
                ("enrollment_total", models.IntegerField()),
                ("enrollment_available", models.IntegerField()),
                ("topic", models.CharField(max_length=100)),
                ("meeting_days", models.CharField(max_length=14)),
                ("start_time", models.TimeField(blank=True, null=True)),
                ("end_time", models.TimeField(blank=True, null=True)),
                ("location", models.CharField(max_length=100)),
                ("book", models.ManyToManyField(to="textbook_exchange.book")),
            ],
        ),
    ]
