import datetime

from django.db import models
from django.contrib.flatpages.models import FlatPage
from django.utils.translation import ugettext_lazy as _

from flatpage_images.conf import settings

class FlatPageImage(models.Model):
    flatpage = models.ForeignKey(FlatPage, related_name='images')
    image = models.ImageField(upload_to=settings.FLATPAGE_IMAGES_PATH, verbose_name=_(u'Image'))
    footnote = models.CharField(verbose_name=_(u'Foot Note'), max_length=255, blank=True)
    order = models.PositiveSmallIntegerField(
        verbose_name=_('Order'),
        default=0,
        help_text=_('Allow to modify the order images will be displayed')
    )

    created_at = models.DateTimeField(default=datetime.datetime.now, editable=False)
    updated_at = models.DateTimeField(editable=False)

    class Media:
        verbose_name = _(u'Flat Page Image')
        verbose_name_plural = _(u'Flat Page Images')
        ordering = ('order', )


    def save(self, **kwargs):
        # refresh updated_at value each time it's saved
        self.updated_at = datetime.datetime.now()
        super(FlatPageImage, self).save(**kwargs)

