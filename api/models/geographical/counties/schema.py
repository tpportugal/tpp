import graphene
from graphene_django import DjangoObjectType

from .models import County


class CountyType(DjangoObjectType):
    class Meta:
        model = County


class Query(object):
    county = graphene.Field(CountyType,
                          id=graphene.Int(),
                          slug=graphene.String(),
                          name=graphene.String(),
                          district__slug=graphene.String())

    counties = graphene.List(CountyType)

    def resolve_county(self, info, **kwargs):
        id = kwargs.get('id')
        slug = kwargs.get('slug')
        name = kwargs.get('name')
        district_slug = kwargs.get('district__slug')

        if id is not None:
            return County.objects.get(pk=id)

        if slug is not None:
            return County.objects.get(slug=slug)

        if name is not None:
            return County.objects.get(name=name)

        if district_slug is not None:
            return County.objects.get(district__slug=district_slug)

        return None

    def resolve_counties(self, info, **kwargs):
        return County.objects.all()
