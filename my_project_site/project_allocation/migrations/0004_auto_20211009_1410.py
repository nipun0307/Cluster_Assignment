# Generated by Django 3.2.8 on 2021-10-09 08:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project_allocation', '0003_course_course_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='course_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='course_id_project', to='project_allocation.course'),
        ),
        migrations.CreateModel(
            name='Student_Enrollment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='course_id_enrolled', to='project_allocation.course')),
                ('student_roll_num', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='student_roll_enrolled', to='project_allocation.student')),
            ],
        ),
    ]
