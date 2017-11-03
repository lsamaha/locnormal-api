# locnormal-api
API for libpostal address parse/expand/normalize 

# run
Get the API running in docker container with:
```bash
docker run -p 5017:5017 --name locnormal-api-test lsamaha/locnormal-api
```

# use
Parse an address:
```json
curl http://myhost:5017/parse?address=1+Park+St+Boston+MA+02128
{"house_number": "1", "postcode": "02128", "city": "boston", "state": "ma", "road": "park st"}
```
Normalize an address:
```json
curl http://myhost:5017/normal?address=1+Park+St+Boston+MA+02128
1 park street boston massachusetts 02128
```

# scale
Spin up in an existing ECS cluster with:

```bash
aws ecs register-task-definition --cli-input-json file://ecs-task-def.json
aws ecs run-task --cluster loc-api-dev --task-definition <task-def-arn>
```

#note
This simple container should live in an app subnet and be paired 
with an nginx container in a public subnet to proxy the public load.


