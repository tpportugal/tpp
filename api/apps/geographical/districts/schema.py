import graphene
from graphene_django import DjangoObjectType

from .models import District


class DistrictType(DjangoObjectType):
    class Meta:
        model = District


class Query(object):
    district = graphene.Field(DistrictType,
                              id=graphene.Int(),
                              slug=graphene.String(),
                              name=graphene.String())

    districts = graphene.List(DistrictType)

    def resolve_district(self, info, **kwargs):
        id = kwargs.get('id')
        slug = kwargs.get('slug')
        name = kwargs.get('name')

        if id is not None:
            return District.objects.get(pk=id)

        if slug is not None:
            return District.objects.get(slug=slug)

        if name is not None:
            return District.objects.get(name=name)

        return None

    def resolve_districts(self, info, **kwargs):
        return District.objects.all()
