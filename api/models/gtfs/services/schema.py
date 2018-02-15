import graphene
from graphene_django import DjangoObjectType

from .models import Service


class ServiceType(DjangoObjectType):
    class Meta:
        model = Service


class Query(object):
    service = graphene.Field(ServiceType,
                            id=graphene.Int(),
                            monday=graphene.Int(),
                            tuesday=graphene.Int(),
                            wednesday=graphene.Int(),
                            thursday=graphene.Int(),
                            friday=graphene.Int(),
                            saturday=graphene.Int(),
                            sunday=graphene.Int(),
                            start_date=graphene.String(),
                            end_date=graphene.String())

    services = graphene.List(ServiceType)

    def resolve_service(self, info, **kwargs):
        id = kwargs.get('id')
        monday = kwargs.get('monday')
        tuesday = kwargs.get('tuesday')
        wednesday = kwargs.get('wednesday')
        thursday = kwargs.get('thursday')
        friday = kwargs.get('friday')
        saturday = kwargs.get('saturday')
        sunday = kwargs.get('sunday')
        start_date = kwargs.get('start_date')
        end_date = kwargs.get('end_date')

        if id is not None:
            return Service.objects.get(pk=id)

        if monday is not None:
            return Service.objects.get(monday=monday)

        if tuesday is not None:
            return Service.objects.get(tuesday=tuesday)

        if wednesday is not None:
            return Service.objects.get(wednesday=wednesday)

        if thursday is not None:
            return Service.objects.get(thursday=thursday)

        if friday is not None:
            return Service.objects.get(friday=friday)

        if saturday is not None:
            return Service.objects.get(saturday=saturday)

        if sunday is not None:
            return Service.objects.get(sunday=sunday)

        if start_date is not None:
            return Service.objects.get(start_date=start_date)

        if end_date is not None:
            return Service.objects.get(end_date=end_date)

        return None

    def resolve_services(self, info, **kwargs):
        return Service.objects.all()
