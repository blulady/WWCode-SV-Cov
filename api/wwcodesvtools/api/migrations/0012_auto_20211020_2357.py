# Generated by Django 3.1 on 2021-10-20 23:57

from django.db import migrations

def copy_user_role(apps, schema_editor):
    UserProfile = apps.get_model('api', 'UserProfile')
    User_Team = apps.get_model('api', 'User_Team')
    Role = apps.get_model('api', 'Role')

    qs_userProfile=UserProfile.objects.all()
    for userProfile in qs_userProfile:
        if userProfile.role:
            user = userProfile.user
            role = Role.objects.get(name=userProfile.role)
            userTeam = User_Team(user=user, team=None, role=role)
            userTeam.save()


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_resource'),
    ]

    operations = [
        migrations.RunPython(copy_user_role),
    ]
