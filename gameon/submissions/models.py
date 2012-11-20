from django.db import models

from tower import ugettext_lazy as _

from managers import ChallengeManager


class Challenge(models.Model):

    objects = ChallengeManager()

    name = models.CharField(max_length=200, verbose_name=(u'Challenge name'),
        unique=True)
    slug = models.SlugField(max_length=100, unique=True,
        verbose_name=_(u'Slug'))
    start_date = models.DateTimeField(verbose_name=_(u'Start date'))
    end_date = models.DateTimeField(verbose_name=_(u'End date'))

    def __unicode__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name=_(u'Display name'),
        unique=True)
    slug = models.SlugField(max_length=100,
        unique=True, verbose_name=_(u'Slug'))

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Categories'


class Entry(models.Model):
    title = models.CharField(max_length=255, verbose_name=_(u'Entry title'),
        unique=True)
    slug = models.SlugField(max_length=255,
        unique=True, verbose_name=_(u'Slug'))
    url = models.URLField(verbose_name=_(u'URL'), max_length=255)
    description = models.TextField(verbose_name=_(u'Description'))
    category = models.OneToOneField(Category, verbose_name=_(u'Category'))

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Entries'
