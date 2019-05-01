# Generated by Django 2.2 on 2019-05-01 09:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('booking', '0007_auto_20190430_1541'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=100)),
                ('method', models.CharField(choices=[('credit card', 'Credit card'), ('debit card', 'Debit card'), ('paypal', 'PayPal')], default='credit card', max_length=20)),
                ('card_name', models.CharField(max_length=100)),
                ('card_number', models.IntegerField()),
                ('card_date', models.CharField(max_length=5)),
                ('card_cvv', models.IntegerField()),
                ('booking', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booking.Booking')),
            ],
        ),
    ]