# Generated by Django 3.2.16 on 2023-07-23 10:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0040_remove_userprofile_followed_communities'),
        ('buyandsell', '0008_alter_product_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='followers',
            field=models.ManyToManyField(blank=True, related_name='productsfollowed', to='users.UserProfile'),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_image',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='users.userprofile'),
        ),
    ]
