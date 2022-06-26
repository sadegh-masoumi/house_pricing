from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView
from .models import Comment


class Home(TemplateView):
    """home view"""
    template_name = 'home.html'


class SendEmail(View):
    """
    home page footer send feedback
    """
    def post(self, request):
        full_name = request.POST.get('name')
        text = request.POST.get('message')
        email = request.POST.get('email')

        Comment.objects.create(
            full_name=full_name,
            text=text,
            email=email
        )
        return render(request, 'home.html', {'email_sent': 'success'})
