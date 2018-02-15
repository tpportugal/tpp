import graphene
from graphene_django.debug import DjangoDebug

from api.models.geographical.counties import schema as CountySchema
from api.models.geographical.districts import schema as DistrictSchema
from api.models.geographical.places import schema as PlaceSchema
from api.models.gtfs.agencies import schema as AgencySchema
from api.models.gtfs.calendardates import schema as CalendarDateSchema
from api.models.gtfs.routes import schema as RouteSchema
from api.models.gtfs.services import schema as ServiceSchema
from api.models.gtfs.stops import schema as StopSchema
from api.models.gtfs.trips import schema as TripSchema


class Query(DistrictSchema.Query,
            CountySchema.Query,
            PlaceSchema.Query,
            AgencySchema.Query,
            CalendarDateSchema.Query,
            RouteSchema.Query,
            ServiceSchema.Query,
            StopSchema.Query,
            TripSchema.Query,
            graphene.ObjectType):
    debug = graphene.Field(DjangoDebug, name='__debug')


schema = graphene.Schema(query=Query)
