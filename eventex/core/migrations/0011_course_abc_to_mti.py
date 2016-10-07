# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-10-07 18:01
from __future__ import unicode_literals

from django.db import migrations


def forward_course_abc_to_mti(apps, schema_editor):
    CourseAbc = apps.get_model('core', 'CourseOld')
    CourseMti = apps.get_model('core', 'Course')

    copy_src_to_dst(CourseAbc, CourseMti)


def backward_course_abc_to_mti(apps, schema_editor):
    CourseAbc = apps.get_model('core', 'CourseOld')
    CourseMti = apps.get_model('core', 'Course')

    copy_src_to_dst(CourseMti, CourseAbc)


def copy_src_to_dst(Source, Destination):
    for src in Source.objects.all():
        dst = Destination(
            title = src.title,
            start = src.start,
            description = src.description,
            slots = src.slots
        )
        dst.save()
        dst.speakers.set(src.speakers.all())
        src.delete()


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_course'),
    ]

    operations = [
        migrations.RunPython(forward_course_abc_to_mti,
                             backward_course_abc_to_mti)
    ]
