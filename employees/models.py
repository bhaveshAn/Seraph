from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from companies.models import Company


class Employee(models.Model):
    """
    Team Member belonging to a Team
    """
    email = models.EmailField(_('email'), max_length=40,
                              unique=True)
    headline = models.CharField(_('headline'), max_length=70,
                                blank=True, null=True)
    website = models.URLField(_('website'), max_length=70,
                              blank=True, null=True)
    linkedin = models.URLField(_('linkedin'), max_length=70,
                               blank=True, null=True)
    github = models.URLField(_('github'), max_length=70,
                             blank=True, null=True)
    twitter = models.URLField(_('twitter'), max_length=70,
                              blank=True, null=True)
    angelist = models.URLField(_('angelist'), max_length=70,
                               blank=True, null=True)
    blog = models.URLField(_('blog'), max_length=70,
                           blank=True, null=True)
    phone = models.CharField(max_length=10, blank=True,
                             null=True)
    skills = models.TextField(_('skills'), blank=True,
                              null=True)
    achivements = models.TextField(_('achivements'), blank=True, null=True)
    user = models.ForeignKey(User, blank=True, null=True, default=None)
    company = models.ForeignKey(Company, blank=True, null=True, default=None)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _('employee')
        verbose_name_plural = _('employees')
