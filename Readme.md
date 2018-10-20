

# Sample application showcasing simple CRUD web APIs

  
Internal member management APIs,  
  
`GET /api/users/` -> list all resources  
  
`GET /api/users/:id/ ` -> get resource record detail  
   
`POST /api/users/` -> create a resource record  
  
`PUT /api/users/:id/` -> update the entire resource record  
  
`PATCH /api/users/:id/` -> partial update the resource record  
  
`DELETE /api/users/:id/` -> delete resource record  
  
  
To run the project, make sure you have following installed.

 - [ ] `docker` 
 - [ ]  `docker-compose` 
  

## Run the project


at terminal

  
```docker-compose up```  
  
  

## Import the initial data


at terminal

`. import_fixtures.sh`  
  
  
  

## Run tests

at terminal  

```docker-compose exec web python manage.py test```



Note: The application consists of two similar models, Members and Users. With the open endingness of requirements,



