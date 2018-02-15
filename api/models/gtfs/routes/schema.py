import graphene
from graphene_django import DjangoObjectType

from .models import Route


class RouteType(DjangoObjectType):
    class Meta:
        model = Route


class Query(object):
    route = graphene.Field(RouteType,
                          id=graphene.Int(),
                          short_name=graphene.String(),
                          long_name=graphene.String(),
                          type=graphene.Int(),
                          agency__slug=graphene.String())

    routes = graphene.List(RouteType)

    def resolve_route(self, info, **kwargs):
        id = kwargs.get('id')
        short_name = kwargs.get('short_name')
        long_name = kwargs.get('long_name')
        transport_type = kwargs.get('type')
        agency_slug = kwargs.get('agency__slug')

        if id is not None:
            return Route.objects.get(pk=id)

        if short_name is not None:
            return Route.objects.get(short_name=short_name)

        if long_name is not None:
            return Route.objects.get(long_name=long_name)

        if transport_type is not None:
            return Route.objects.get(type=transport_type)

        if agency_slug is not None:
            return Route.objects.get(agency__slug=agency_slug)

        return None

    def resolve_routes(self, info, **kwargs):
        return Route.objects.all()
