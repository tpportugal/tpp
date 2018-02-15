import graphene
from graphene_django import DjangoObjectType

from .models import Stoptime


class StoptimeType(DjangoObjectType):
    class Meta:
        model = Stoptime


class Query(object):
    stoptime = graphene.Field(StoptimeType,
                          id=graphene.Int(),
                          trip__pk=graphene.Int(),
                          stop__pk=graphene.Int(),
                          stop__sequence=graphene.Int(),
                          arrival_time=graphene.String(),
                          departure_time=graphene.String())

    stoptimes = graphene.List(StoptimeType)

    def resolve_stoptime(self, info, **kwargs):
        id = kwargs.get('id')
        trip_pk = kwargs.get('trip__pk')
        stop_pk = kwargs.get('stop__pk')
        stop_sequence = kwargs.get('stop_sequence')
        arrival_time = kwargs.get('arrival_time')
        departure_time = kwargs.get('departure_time')

        if id is not None:
            return Stoptime.objects.get(pk=id)

        if trip_pk is not None:
            return Stoptime.objects.get(trip__pk=trip_pk)

        if stop_pk is not None:
            return Stoptime.objects.get(stop__pk=stop_pk)

        if stop_sequence is not None:
            return Stoptime.objects.get(stop_sequence=stop_sequence)

        if arrival_time is not None:
            return Stoptime.objects.get(arrival_time=arrival_time)

        if departure_time is not None:
            return Stoptime.objects.get(departure_time=departure_time)

        return None

    def resolve_stoptimes(self, info, **kwargs):
        return Stoptime.objects.all()
