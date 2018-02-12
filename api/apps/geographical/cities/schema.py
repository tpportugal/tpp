import graphene
from graphene_django import DjangoObjectType

from .models import City


class CityType(DjangoObjectType):
    class Meta:
        model = City


class Query(object):
    city = graphene.Field(CityType,
                          id=graphene.Int(),
                          slug=graphene.String(),
                          name=graphene.String(),
                          district__slug=graphene.String())

    cities = graphene.List(CityType)

    def resolve_city(self, info, **kwargs):
        id = kwargs.get('id')
        slug = kwargs.get('slug')
        name = kwargs.get('name')
        district_slug = kwargs.get('district__slug')

        if id is not None:
            return City.objects.get(pk=id)

        if slug is not None:
            return City.objects.get(slug=slug)

        if name is not None:
            return City.objects.get(name=name)

        if district_slug is not None:
            return City.objects.get(district__slug=district_slug)

        return None

    def resolve_cities(self, info, **kwargs):
        return City.objects.all()
