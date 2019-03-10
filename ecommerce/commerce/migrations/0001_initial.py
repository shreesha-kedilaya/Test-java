# Generated by Django 2.1.7 on 2019-03-10 20:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='BillingInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('billingAddress', models.CharField(max_length=250)),
                ('creditCard', models.PositiveIntegerField()),
                ('billDate', models.DateTimeField()),
                ('creditCardPin', models.PositiveSmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('orderNumber', models.PositiveIntegerField()),
                ('orderDate', models.DateTimeField()),
                ('deliveryDate', models.DateTimeField()),
                ('shippedDate', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='PersonalInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=250)),
                ('country', models.CharField(max_length=15)),
                ('phoneNumber', models.CharField(max_length=15)),
                ('postalCode', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productName', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=500)),
                ('price', models.PositiveIntegerField()),
                ('weight', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contactName', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=500)),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
        ),
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='commerce.User')),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('commerce.user',),
        ),
        migrations.CreateModel(
            name='Shipper',
            fields=[
                ('company_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='commerce.Company')),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('commerce.company',),
        ),
        migrations.AddField(
            model_name='user',
            name='personalInfo',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='commerce.PersonalInfo'),
        ),
        migrations.AddField(
            model_name='user',
            name='polymorphic_ctype',
            field=models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='polymorphic_commerce.user_set+', to='contenttypes.ContentType'),
        ),
        migrations.AddField(
            model_name='product',
            name='supplier',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='commerce.User'),
        ),
        migrations.AddField(
            model_name='order',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='commerce.User'),
        ),
        migrations.AddField(
            model_name='company',
            name='personalInfo',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='commerce.PersonalInfo'),
        ),
        migrations.AddField(
            model_name='company',
            name='polymorphic_ctype',
            field=models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='polymorphic_commerce.company_set+', to='contenttypes.ContentType'),
        ),
        migrations.AddField(
            model_name='cart',
            name='products',
            field=models.ManyToManyField(to='commerce.Product'),
        ),
        migrations.AddField(
            model_name='cart',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='commerce.User'),
        ),
        migrations.AddField(
            model_name='order',
            name='shipper',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='commerce.Shipper'),
        ),
    ]
