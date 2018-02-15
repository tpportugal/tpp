#!/bin/bash

# Print out the current docker-compose version. Once this reports 1.6+ then we
# do not need the following steps.
docker-compose --version

# Setup your application stack. You may need to tweak these commands if you
# doing out-of-the-ordinary docker-compose builds.
docker-compose -f docker-compose.development.yml pull
docker-compose -f docker-compose.development.yml build
docker-compose -f docker-compose.development.yml up -d
docker-compose -f docker-compose.development.yml run --rm web python manage.py migrate
