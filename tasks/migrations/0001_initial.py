from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('description', models.TextField(blank=True, null=True)),
                ('due_date', models.DateField(blank=True, null=True)),
                ('priority', models.CharField(choices=[('high', 'High'), ('medium', 'Medium'), ('low', 'Low')], default='medium', max_length=10)),
                ('is_slayed', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('slayed_at', models.DateTimeField(blank=True, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to='auth.user')),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
    ]
