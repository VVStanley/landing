from django.conf import settings
from django.core.mail import send_mail
from django.http import JsonResponse
from django.shortcuts import render
from django.views import View

from .models import Portfolio, InfoCompany


class HomeView(View):

    template_name = 'base.html'

    def get(self, request):
        context = {
            'portfolio_photos': Portfolio.objects.all()
        }
        return render(request, self.template_name, context)


class SendEmail(View):

    def post(self, request):

        info = InfoCompany.objects.get()

        name = request.POST.get('name', None)
        phone = request.POST.get('phone', None)
        subject = request.POST.get('subject', None)

        if info.email and name and phone:
            send_mail(
                'Заявка с сайта',
                f'''
                    Имя - {name};
                    Телефон - {phone};
                    Объект - {subject};
                ''',
                settings.EMAIL_HOST_USER,
                [info.email, ],
                fail_silently=False,
            )

            return JsonResponse({'status': True})
        return JsonResponse({'status': False})
