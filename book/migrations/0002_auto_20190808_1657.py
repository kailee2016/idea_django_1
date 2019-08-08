# Generated by Django 2.1.5 on 2019-08-08 08:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='infobook',
            name='authorID',
            field=models.ForeignKey(db_column='authorid', on_delete=django.db.models.deletion.DO_NOTHING, to='book.InfoAuthor'),
        ),
        migrations.AlterField(
            model_name='infobook',
            name='lbID',
            field=models.ForeignKey(db_column='lbid', on_delete=django.db.models.deletion.DO_NOTHING, to='book.InfoBookLb'),
        ),
        migrations.AlterField(
            model_name='infobook',
            name='pubid',
            field=models.ForeignKey(db_column='pubid', on_delete=django.db.models.deletion.DO_NOTHING, to='book.InfoPublisher'),
        ),
    ]
