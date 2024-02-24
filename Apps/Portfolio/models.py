from django.db import models
from django.utils.translation import gettext_lazy as _
# Create your models here.


class TechnologyModel(models.Model):
    tech = models.CharField(
        _("Tecnologías"), max_length=150, unique=True
    )

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Technology'
        verbose_name_plural = 'Technologies'
        ordering = ['-id']

    def __str__(self) -> str:
        return self.tech


class ProjectModel(models.Model):
    title = models.CharField(_("Nombre del Proyecto"), max_length=150)
    description = models.TextField(_("Descripción"), blank=True)
    img = models.ImageField(_("Imagen Proyecto"),
                            upload_to='Proyectos/', blank=True)
    url = models.URLField(_("Enlace"), blank=True)
    used = models.ManyToManyField(TechnologyModel, blank=True)

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'
        ordering = ['-id']

    def __str__(self) -> str:
        return self.title


def cv_file_path(instance, filename):
    filename = 'cv.pdf'
    return 'cv/{0}'.format(filename)


class Cv(models.Model):
    cv = models.FileField(_("CV"), upload_to=cv_file_path, blank=True)

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'CV'
        verbose_name_plural = 'CV'
        ordering = ['-id']
