from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin

from app_apartment.models import Address
from .algorithm import predict


def by_check(value):
    return True if value is not None else False


class Prediction(LoginRequiredMixin, View):
    def get(self, request):
        locations = Address.objects.all()
        locations = sorted(locations.values_list('name', flat=True))
        return render(request, 'prediction.html', {
            'locations': locations
        })

    def post(self, request):
        room = int(request.POST.get('room'))
        area = int(request.POST.get('area'))
        address = request.POST.get('address')
        has_elevator = by_check(request.POST.get('has_elevator'))
        has_parking = by_check(request.POST.get('has_parking'))
        has_warehouse = by_check(request.POST.get('has_warehouse'))

        address = Address.objects.filter(
            name__icontains=address.lower()
        )
        if not address.exists():
            return render(request, 'prediction.html', {
                'message': 'not_valid_address'
            })
        address = address[0].id
        price = predict(area,
                        room,
                        has_parking,
                        has_warehouse,
                        has_elevator,
                        address
                        )
        return render(request, 'prediction.html', {
            'predict': True, 'price': price
        })
