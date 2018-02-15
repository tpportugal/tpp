import graphene
from graphene_django import DjangoObjectType

from .models import Place


class PlaceType(DjangoObjectType):
    class Meta:
        model = Place


class Query(object):
    place = graphene.Field(PlaceType,
                          id=graphene.Int(),
                          slug=graphene.String(),
                          name=graphene.String(),
                          county__slug=graphene.String())

    places = graphene.List(PlaceType)

    def resolve_place(self, info, **kwargs):
        id = kwargs.get('id')
        slug = kwargs.get('slug')
        name = kwargs.get('name')
        county_slug = kwargs.get('county__slug')

        if id is not None:
            return Place.objects.get(pk=id)

        if slug is not None:
            return Place.objects.get(slug=slug)

        if name is not None:
            return Place.objects.get(name=name)

        if county_slug is not None:
            return Place.objects.get(county__slug=county_slug)

        return None

    def resolve_places(self, info, **kwargs):
        return Place.objects.all()
