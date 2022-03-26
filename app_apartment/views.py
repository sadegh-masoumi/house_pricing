from django.shortcuts import render
from .models import Address, Apartment
from django.views.generic import ListView
from django.views import View
from django.core.paginator import Paginator, EmptyPage
from django.contrib.auth.mixins import LoginRequiredMixin


class PaginatorView(Paginator, LoginRequiredMixin):
    def validate_number(self, number):
        try:
            return super().validate_number(number)
        except EmptyPage:
            if int(number) > 1:
                # return the last page
                return self.num_pages
            elif int(number) < 1:
                # return the first page
                return 1
            else:
                raise


def by_check(value):
    return True if value is not None else False


class ApartmentList(ListView, LoginRequiredMixin):
    template_name = 'apartment_list.html'
    model = Apartment
    paginate_by = 30
    paginator_class = PaginatorView
    context_object_name = 'apartment_list'

    def get_queryset(self):
        return self.model.objects.all()


class ApartmentListUser(ListView, LoginRequiredMixin):
    template_name = 'apartment_list.html'
    model = Apartment
    paginate_by = 30
    paginator_class = PaginatorView
    context_object_name = 'apartment_list'

    def get_queryset(self):
        queryset = self.model.objects.filter(person__email=self.kwargs.get('email'))
        return queryset


class ApartmentCreate(View, LoginRequiredMixin):
    def post(self, request):
        room = request.POST.get('room')
        area = request.POST.get('area')
        address = request.POST.get('address').strip()
        price = request.POST.get('price').strip().replace(',', '')
        has_parking = by_check(request.POST.get('has_parking'))
        has_elevator = by_check(request.POST.get('has_elevator'))
        has_warehouse = by_check(request.POST.get('has_warehouse'))
        try:
            Apartment.objects.create(
                room=room,
                area=area,
                address=Address.objects.get(name=address),
                price=price,
                has_parking=has_parking,
                has_elevator=has_elevator,
                has_warehouse=has_warehouse,
                person=request.user
            )
            return render(request, 'dashboard.html', {'message': 'added_successfully'})
        except:
            return render(request, 'dashboard.html', {
                'message': 'not_added',
                'room': room,
                'area': area,
                'address': address,
                'price': price,
                'has_parking': has_parking,
                'has_elevator': has_elevator,
                'has_warehouse': has_warehouse
            })
