#!/usr/bin/env bash

docker-compose exec web python manage.py loaddata users/fixtures/01.json --app users.User

