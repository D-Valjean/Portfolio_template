from django.contrib import admin
from .models import ProjectModel, TechnologyModel, Cv
# Register your models here.


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'url')
    search_fields = ('title',)


admin.site.register(ProjectModel, ProjectAdmin)
admin.site.register(TechnologyModel)
admin.site.register(Cv)

admin.site.site_header = 'Panel Administrador'
admin.site.site_title = 'Proyectos'
admin.site.index_title = 'Proyectos'  # esquina superior izquierda
