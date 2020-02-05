# Generated by Django 2.2.7 on 2019-11-19 13:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BankInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('bank_id', models.CharField(max_length=5)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='BranchInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('branch_name', models.CharField(max_length=256)),
                ('ifsc', models.CharField(max_length=500, unique=True)),
                ('address', models.TextField()),
                ('city', models.CharField(max_length=500)),
                ('district', models.CharField(max_length=500)),
                ('state', models.CharField(max_length=500)),
                ('bank', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bank_info.BankInfo')),
            ],
        ),
    ]