import graphene
from graphene_django import DjangoObjectType

from .models import Trip


class TripType(DjangoObjectType):
    class Meta:
        model = Trip


class Query(object):
    trip = graphene.Field(TripType,
                          id=graphene.Int(),
                          route__pk=graphene.Int(),
                          calendardate__pk=graphene.Int())

    trips = graphene.List(TripType)

    def resolve_trip(self, info, **kwargs):
        id = kwargs.get('id')
        route_pk = kwargs.get('route__pk')
        calendardate_pk = kwargs.get('calendardate__pk')

        if id is not None:
            return Trip.objects.get(pk=id)

        if route_pk is not None:
            return Trip.objects.get(route__pk=route_pk)

        if calendardate_pk is not None:
            return Trip.objects.get(calendardate__pk=calendardate_pk)

        return None

    def resolve_trips(self, info, **kwargs):
        return Trip.objects.all()
