# Generated by Django 4.1 on 2022-10-08 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkup', '0007_alter_patient_gender_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patientvisit',
            name='Have_you_ever_been_on_diet',
            field=models.CharField(choices=[('yes', 'Yes'), ('No', 'No')], max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='patientvisit',
            name='general_health',
            field=models.CharField(choices=[('Good', 'Good'), ('Poor', 'Poor')], max_length=4, null=True),
        ),
    ]
