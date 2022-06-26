import datetime
import pandas as pd
import numpy as np

from app_apartment.models import Apartment, Address


def predict(area, room, has_parking, has_warehouse, has_elevator, address):
    df = pd.DataFrame(list(Apartment.objects.all().values(
        'area',
        'room',
        'has_parking',
        'has_warehouse',
        'has_elevator',
        'address',
        'price'
    )))
    df.columns = [
        'area',
        'room',
        'has_parking',
        'has_warehouse',
        'has_elevator',
        'address',
        'price'
    ]
    df = df[df['address'] == address]
    # normalize of area and room
    df['area'] = (df['area'] - df['area'].min()) / (df['area'].max() - df['area'].min())
    df['room'] = (df['room'] - df['room'].min()) / (df['room'].max() - df['room'].min())
    # KNN - Regression
    df['euclid'] = np.sqrt(
        (df['area'] - area) ** 2 +
        (df['room'] - room) ** 2 +
        (df['has_parking'] - int(has_parking)) ** 2 +
        (df['has_warehouse'] - int(has_warehouse)) ** 2 +
        (df['has_elevator'] - int(has_elevator)) ** 2 +
        (df['address'] - address) ** 2
    )
    price = df.sort_values('euclid')[:2].mean()['price']
    return "%.2f" % (price / 1_000_000_000)
