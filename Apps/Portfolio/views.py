import os
from django.conf import settings
from django.views.generic import TemplateView
from .models import ProjectModel, TechnologyModel
from django.core.mail import EmailMessage
from django.http.response import HttpResponseRedirect
# Create your views here.


class PortfolioView(TemplateView):
    template_name = "portfolio/portfolio.html"
    sucess_url = '/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        title = 'titulo'
        all_tech = TechnologyModel.objects.all()
        all_projects = ProjectModel.objects.all().order_by('id')
        linkein = "https://www.linkedin.com/"
        git = "https://github.com/"
        email = "tu_correo@gmail.com"
        cv = os.path.join(
            settings.MEDIA_URL, 'cv/cv.pdf')
        you_name = "Tu Nombre"
        you_title = "Tu Titulo"  # example Ing.
        context["title"] = title
        context["all_tech"] = all_tech
        context["all_projects"] = all_projects
        context["linkein"] = linkein
        context["git"] = git
        context["email"] = email
        context["you_name"] = you_name
        context["you_title"] = you_title
        context["cv"] = cv
        return context

    def post(self, request, *args, **kwargs):
        subject = request.POST['email'] + "| Nombre: " + request.POST['name']
        message = request.POST['message']
        email_from = settings.EMAIL_HOST_USER
        recipient_list = ['correo_de_destino@gmail.com']
        email = EmailMessage(subject, message, email_from, recipient_list)
        email.send()
        return HttpResponseRedirect(self.sucess_url)
