from django.db import models
from django.utils.translation import ugettext as _
from django.utils.timezone import now
from django.utils.functional import cached_property

# from HTMLParser import HTMLParser


try:
    from django.contrib.auth import get_user_model
    User = get_user_model()
except:
    from django.conf import settings
    User = settings.AUTH_USER_MODEL


class PollManager(models.Manager):
    def current(self):
        try:
            return self.filter(
                beginning__lt=now(),
                end__gt=now(),
            ).annotate(
                votes_count=models.Count('choices__votes')
            )[0]
        except IndexError:
            return self.annotate(
                votes_count=models.Count('choices__votes')
            ).latest()


class Poll(models.Model):

    class Meta:
        verbose_name = _('poll')
        verbose_name_plural = _('polls')
        get_latest_by = 'end'
        ordering = ('-end', )

    title = models.CharField(
        _('title'),
        max_length=255,
    )
    beginning = models.DateTimeField(
        _('beginning'),
        default=now,
    )
    end = models.DateTimeField(
        _('end'),
    )

    objects = PollManager()

    def __unicode__(self):
        return self.title

    def vote_for(self, user):
        try:
            return self.choices.get(votes__user=user)
        except Choice.DoesNotExist:
            return None
    vote_for.short_description = _('vote for ?')


class Choice(models.Model):
    class Meta:
        verbose_name = _('choice')
        verbose_name_plural = _('choices')

    poll = models.ForeignKey(
        Poll,
        verbose_name=_('poll'),
        related_name='choices',
    )

    value = models.CharField(
        _('value'),
        max_length=255,
    )

    @cached_property
    def stripped_value(self):
        return self.value.strip()

    def __unicode__(self):
        return self.value


class Vote(models.Model):

    class Meta:
        verbose_name = _('vote')
        verbose_name_plural = _('votes')
        unique_together = (
            ('user', 'choice', ),
        )

    choice = models.ForeignKey(
        Choice,
        verbose_name=_('choice'),
        related_name='votes',
    )

    user = models.ForeignKey(
        User,
        verbose_name=_('user'),
        related_name='votes',
    )
