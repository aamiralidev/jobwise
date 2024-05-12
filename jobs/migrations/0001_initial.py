# Generated by Django 4.2.2 on 2024-05-12 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BoardProvider',
            fields=[
                ('identifier', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('domain', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('identifier_by_prefix', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('original_id', models.CharField(blank=True, max_length=255)),
                ('title', models.CharField(max_length=255)),
                ('company_name', models.CharField(max_length=255)),
                ('company_website', models.URLField(blank=True)),
                ('company_logo', models.ImageField(blank=True, null=True, upload_to='company_logos/')),
                ('career_level', models.CharField(blank=True, choices=[('intern', 'Intern'), ('apprenticeship', 'Apprenticeship'), ('freshgrad', 'Fresh Graduate'), ('associate', 'Associate'), ('entry', 'Entry'), ('mid', 'Mid'), ('senior', 'Senior'), ('staff', 'Staff'), ('director', 'Director'), ('executive', 'Executive')], max_length=50)),
                ('experience_level_min', models.IntegerField(default=-1)),
                ('experience_level_max', models.IntegerField(default=-1)),
                ('date_posted', models.DateField(auto_now_add=True)),
                ('degree', models.CharField(choices=[('bachelors', "Bachelor's"), ('masters', "Master's"), ('phd', 'PhD'), ('diploma', 'Diploma'), ('no_degree_required', 'No Degree Required')], default='no_degree_required', max_length=50)),
                ('visa_sponsorship', models.BooleanField(default=False)),
                ('remote_from_anywhere', models.BooleanField(default=False)),
                ('relocation_support', models.BooleanField(default=False)),
                ('job_role', models.CharField(blank=True, max_length=100)),
                ('skills', models.CharField(blank=True, max_length=255)),
                ('language', models.CharField(blank=True, max_length=100)),
                ('contract', models.CharField(choices=[('temporary', 'Temporary'), ('permanent', 'Permanent')], default='permanent', max_length=50)),
                ('commitment', models.CharField(choices=[('part-time', 'Part-time'), ('full-time', 'Full-time')], default='full-time', max_length=50)),
                ('workplace_type', models.CharField(choices=[('on-site', 'On-site'), ('remote', 'Remote'), ('hybrid', 'Hybrid'), ('remote-across-borders', 'Remote across Borders')], default='on-site', max_length=50)),
                ('region', models.CharField(blank=True, max_length=255)),
                ('country', models.CharField(blank=True, max_length=255)),
                ('state', models.CharField(blank=True, max_length=255)),
                ('city', models.CharField(blank=True, max_length=255)),
                ('location', models.CharField(blank=True, max_length=255)),
                ('job_description', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='JobBoard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('provider', models.CharField(blank=True, max_length=255)),
                ('identifier', models.CharField(max_length=255)),
                ('company_name', models.CharField(max_length=255)),
                ('board_url', models.CharField(max_length=255)),
            ],
            options={
                'unique_together': {('provider', 'identifier')},
            },
        ),
    ]