import graphene
from graphene_django import DjangoObjectType

from .models import CalendarDate


class CalendarDateType(DjangoObjectType):
    class Meta:
        model = CalendarDate


class Query(object):
    calendardate = graphene.Field(CalendarDateType,
                          id=graphene.Int(),
                          service__pk=graphene.Int(),
                          date=graphene.String(),
                          exception_type=graphene.Int())

    calendardates = graphene.List(CalendarDateType)

    def resolve_calendardate(self, info, **kwargs):
        id = kwargs.get('id')
        service_pk = kwargs.get('service__pk')
        date = kwargs.get('date')
        exception_type = kwargs.get('exception_type')

        if id is not None:
            return CalendarDate.objects.get(pk=id)

        if service_pk is not None:
            return CalendarDate.objects.get(service__pk=service_pk)

        if date is not None:
            return CalendarDate.objects.get(date=date)

        if exception_type is not None:
            return CalendarDate.objects.get(exception_type=exception_type)

        return None

    def resolve_calendardates(self, info, **kwargs):
        return CalendarDate.objects.all()
