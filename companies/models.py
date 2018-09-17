from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User


class Company(models.Model):
    """
    Team Member belonging to a Team
    """
    email = models.EmailField(_('email'), max_length=40, unique=True)
    name = models.CharField(_('name'), max_length=30)
    location = models.CharField(_('location'), max_length=50)
    domain = models.CharField(_('domain'), max_length=70, blank=True,
                              null=True)
    website = models.URLField(_('website'), max_length=70)
    linkedin = models.URLField(_('linkedin'), max_length=70, blank=True,
                               null=True)
    github = models.URLField(_('github'), max_length=70, blank=True, null=True)
    twitter = models.URLField(_('twitter'), max_length=70, blank=True,
                              null=True)
    angelist = models.URLField(_('angelist'), max_length=70, blank=True,
                               null=True)
    blog = models.URLField(_('blog'), max_length=70, blank=True, null=True)
    phone = models.CharField(max_length=10)
    achivements = models.TextField(_('achivements'), blank=True, null=True)
    admin = models.ForeignKey(User, blank=True, null=True, default=None)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _('company')
        verbose_name_plural = _('companies')
