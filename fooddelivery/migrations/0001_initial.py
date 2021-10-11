# Generated by Django 3.2.7 on 2021-10-03 07:47

from django.db import migrations, models
import django.db.models.deletion
import django.db.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Foods',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('photo', models.CharField(max_length=40)),
                ('calorie', models.FloatField()),
                ('fats', models.FloatField()),
                ('carbs', models.FloatField()),
                ('protien', models.FloatField()),
                ('addn_nuti_info', models.CharField(max_length=25)),
                ('description', models.CharField(max_length=1000)),
                ('avilability', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30, unique=True)),
                ('name', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=1)),
                ('contact', models.CharField(max_length=10)),
                ('is_chef', models.BooleanField(default=False)),
                ('photo', models.CharField(max_length=40, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stars', models.IntegerField()),
                ('review', models.CharField(max_length=200)),
                ('food', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fooddelivery.foods')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fooddelivery.users')),
            ],
        ),
        migrations.CreateModel(
            name='Payments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=10)),
                ('field1', models.CharField(max_length=50)),
                ('field2', models.CharField(max_length=50)),
                ('field3', models.CharField(max_length=50)),
                ('field4', models.CharField(max_length=50)),
                ('field5', models.CharField(max_length=50)),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fooddelivery.users')),
            ],
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Amount', models.FloatField()),
                ('payment_mode', models.CharField(max_length=3)),
                ('paid', models.BooleanField()),
                ('delivery_address', models.CharField(max_length=100)),
                ('contact_no', models.CharField(max_length=10)),
                ('transaction_no', models.CharField(max_length=30)),
                ('status', models.IntegerField(default=0)),
                ('user_profile', models.ForeignKey(on_delete=django.db.models.fields.NOT_PROVIDED, to='fooddelivery.users')),
            ],
        ),
        migrations.AddField(
            model_name='foods',
            name='chef',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fooddelivery.users'),
        ),
        migrations.CreateModel(
            name='FoodOrdered',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1)),
                ('food', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fooddelivery.foods')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fooddelivery.orders')),
            ],
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1)),
                ('food', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fooddelivery.foods')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fooddelivery.users')),
            ],
        ),
        migrations.CreateModel(
            name='Addresses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=100)),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fooddelivery.users')),
            ],
        ),
    ]
