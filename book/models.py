from django.db import models


# Create your models here.
class InfoBook(models.Model):
    id = models.CharField(primary_key=True, max_length=255, db_column='id')
    isbn = models.CharField(unique=True, null=False, db_column='isbn',max_length=255)
    num = models.PositiveIntegerField(default=0, db_column='num')
    summary = models.TextField(db_column='summary')
    authorID=models.ForeignKey('InfoAuthor',on_delete=models.DO_NOTHING,db_column='authorid')
    lbID=models.ForeignKey('InfoBookLb',on_delete=models.DO_NOTHING,db_column='lbid')
    pubid=models.ForeignKey('InfoPublisher',on_delete=models.DO_NOTHING,db_column='pubid')
    class Meta:
        db_table='infobook'


class InfoAuthor(models.Model):
    id = models.CharField(primary_key=True, max_length=255, db_column='id')
    sex=models.CharField(max_length=3,db_column='sex',default='',null=True)
    name=models.CharField(max_length=255,db_column='name',null=False)
    class Meta:
        db_table='infoauthor'

class InfoBookLb(models.Model):
    id=models.CharField(primary_key=True,max_length=255,db_column='id')
    lbdm=models.CharField(max_length=20,null=False,unique=True,db_column='lbdm')
    lbmc=models.CharField(max_length=255,db_column='lbmc',null=False)
    class Meta:
        db_table='infobooklb'

class InfoPublisher(models.Model):
    id=models.CharField(primary_key=True,max_length=255,db_column='id')
    name=models.CharField(null=False,max_length=255,db_column='name',unique=True)
    city=models.CharField(null=True,max_length=255,db_column='city')
    class Meta:
        db_table='infopublisher'
