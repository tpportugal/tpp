import graphene
from graphene_django import DjangoObjectType

from .models import Agency


class AgencyType(DjangoObjectType):
    class Meta:
        model = Agency


class Query(object):
    agency = graphene.Field(AgencyType,
                          id=graphene.Int(),
                          slug=graphene.String(),
                          name=graphene.String(),
                          url=graphene.String(),
                          timezone=graphene.String())

    agencies = graphene.List(AgencyType)

    def resolve_agency(self, info, **kwargs):
        id = kwargs.get('id')
        slug = kwargs.get('slug')
        name = kwargs.get('name')
        url = kwargs.get('url')
        timezone = kwargs.get('timezone')

        if id is not None:
            return Agency.objects.get(pk=id)

        if slug is not None:
            return Agency.objects.get(slug=slug)

        if name is not None:
            return Agency.objects.get(name=name)

        if url is not None:
            return Agency.objects.get(url=url)

        if timezone is not None:
            return Agency.objects.get(timezone=timezone)

        return None

    def resolve_agencies(self, info, **kwargs):
        return Agency.objects.all()
