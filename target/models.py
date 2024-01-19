from django.db import models
from django.utils.translation import gettext as _
from django.utils import timezone

# Create your models here.
class Target(models.Model):
    name = models.CharField(_("Nome"), max_length=255, null=False, blank=False)
    geocode = models.CharField(_("Latitude e longitude"), max_length=64, null=False, blank=False)
    expire_date = models.DateField(_("Data de expiração"), null=False, blank=False)
    creation_datetime = models.DateTimeField(_("Data de criação"), editable=False)
    edition_datetime = models.DateTimeField(_("Última atualização"), null=True, blank=True)
    
    class Meta:
        ordering = ('-creation_datetime',)
        verbose_name = _('Alvo')
        verbose_name_plural = _('Alvos')
    
    def save(self, *args, **kwargs):
        # Atualizar datas criacao edicao
        if not self.creation_datetime:
            self.creation_datetime = timezone.now()
        self.edition_datetime = timezone.now()
        
        return super(Target, self).save(*args, **kwargs)