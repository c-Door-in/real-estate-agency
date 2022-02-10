# Generated by Django 2.2.24 on 2022-02-10 21:07

from django.db import migrations


def copy_owners(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    Owner = apps.get_model('property', 'Owner')
    for flat in Flat.objects.all():
        Owner.objects.get_or_create(
            name=flat.owner,
            phonenumber=flat.owners_phonenumber,
            defaults={
                'pure_phone': flat.owner_pure_phone,
            },
        )


def move_backward(apps, schema_editor):
    Owner = apps.get_model('property', 'Owner')
    Owner.objects.all().delete()


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0011_owner'),
    ]

    operations = [
        migrations.RunPython(copy_owners)
    ]
