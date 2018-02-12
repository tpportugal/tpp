import graphene
from graphene_django.debug import DjangoDebug

from api.models.geographical.cities import schema as CitySchema
from api.models.geographical.districts import schema as DistrictSchema


class Query(DistrictSchema.Query,
            CitySchema.Query,
            graphene.ObjectType):
    debug = graphene.Field(DjangoDebug, name='__debug')


schema = graphene.Schema(query=Query)
