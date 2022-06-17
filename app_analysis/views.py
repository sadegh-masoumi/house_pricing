import random
from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin

from app_apartment.models import Apartment
from app_apartment.models import Address

from django.db.models import Avg, Count


class Analysis(LoginRequiredMixin, View):
    """
    simple report of price and count of apartment and address
    """

    def get(self, request):
        valid_loc_id_list = Address.objects.all().values_list('id', flat=True)

        random_loc_id_list = []
        while len(random_loc_id_list) != 10:
            choice = random.choice(valid_loc_id_list)
            if choice not in random_loc_id_list:
                random_loc_id_list.append(choice)

        locations = Address.objects.filter(id__in=random_loc_id_list)

        # find average of price for 10 random location in tehran
        mean_prices = []
        for loc in locations:
            mean = Apartment.objects.filter(address=loc).aggregate(Avg('price'))['price__avg']
            mean_prices.append(mean / 10 ** 6)

        # find average of price for house by 0 to 6 rooms
        mean_price_room = []
        for room in range(6):
            mean = Apartment.objects.filter(room=room).aggregate(Avg('price'))['price__avg']
            mean_price_room.append(mean / 10 ** 6)

        apartments_stats = {
            'tehran': len(Apartment.objects.all()),
            'tajrish': len(Apartment.objects.filter(address__name='Tajrish')),
            'pasdaran': len(Apartment.objects.filter(address__name='Pasdaran'))
        }

        price_stats = {
            'tehran': Apartment.objects.all().aggregate(Avg('price'))['price__avg'] / 10 ** 9,
            'tajrish': Apartment.objects.filter(address__name='Tajrish').aggregate(Avg('price'))[
                           'price__avg'] / 10 ** 9,
            'pasdaran': Apartment.objects.filter(address__name='Pasdaran').aggregate(Avg('price'))[
                            'price__avg'] / 10 ** 9
        }

        room_stats = {
            'tehran': Apartment.objects.all().aggregate(Avg('room'))['room__avg'],
            'tajrish': Apartment.objects.filter(address__name='Tajrish').aggregate(Avg('room'))['room__avg'],
            'pasdaran': Apartment.objects.filter(address__name='Pasdaran').aggregate(Avg('room'))['room__avg']
        }

        ordered_address = Address.objects.all().annotate(Count('apartment')).order_by('-apartment__count')

        loc_stats = {
            'tehran': len(Address.objects.all()),
            'first': ordered_address.first().name,
            'second': ordered_address.last().name,
        }

        return render(request, 'analysis.html', {
            'locations': locations,
            'mean_prices': mean_prices,
            'mean_price_room': mean_price_room,
            'apartments_stats': apartments_stats,
            'price_stats': price_stats,
            'room_stats': room_stats,
            'loc_stats': loc_stats
        })
