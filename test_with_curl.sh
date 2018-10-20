#!/usr/bin/env bash

# list all
curl -i http://127.0.0.1:8000/api/users/


# create resource
curl --header "Content-Type: application/json" \
  --request POST \
  --data '{"first_name":"Karan","last_name":"Kumar", "role": "1", "username": "karan.kumar1112"}' \
  http://127.0.0.1:8000/api/users/


#update a resource
curl -X PATCH -H "Content-type: application/json" -d '{"first_name": "Karan","last_name": "Kumar"}'\
 http://127.0.0.1:8000/api/users/91ba05c9-fea9-48b1-8d31-4412b19f5d07/


# delete a resource
curl -X DELETE http://127.0.0.1:8000/api/users/91ba05c9-fea9-48b1-8d31-4412b19f5d07/
