#!/bin/bash

# update is required to update the repositories to see the new packages for
# Docker.
sudo apt-get update

# Now we can install the newer docker-engine which is required for the newer
# docker-composer we will install next. The messy options are to force it to
# be non-interactive (normally it asks you a bunch of config questions).
sudo apt-get install -o Dpkg::Options::="--force-confold" --force-yes -y docker-ce

# Print out the current docker-compose version. Once this reports 1.6+ then we
# do not need the following steps.
docker-compose --version

# Setup your application stack. You may need to tweak these commands if you
# doing out-of-the-ordinary docker-compose builds.
docker-compose -f docker-compose.development.yml pull
docker-compose -f docker-compose.development.yml build
docker-compose -f docker-compose.development.yml up -d
docker-compose -f docker-compose.development.yml run --rm web python manage.py migrate

# Start development version of the project
sudo bash start_development.sh