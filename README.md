# Minimal Flask API

Run with:
```sh
docker build -t sample-flask-api .
docker run -d --network host --name flask-api sample-flask-api:latest
```

## Sample Test Curl Requests

<details>
<summary>1. Get Appointments</summary>

```sh
curl 'http://localhost:5000/users/1/appointments'
```

*Assumptions: if the user sends a broken time it'll be rounded to the nearest sharp 00 or 30min
</details>


<details>
<summary>2. Create Appointments</summary>

```sh
curl --request POST 'http://localhost:5000/appointments/create' \
--header 'Content-Type: application/json' \
--data-raw '{
    "user": "4",
    "time": "2021-02-22 12:30:00"
}'
```
</details>


<details>
<summary>3. Create User</summary>

```sh
curl --request POST 'http://localhost:5000/users/create' \
--header 'Content-Type: application/json' \
--data-raw '{
    "user": "4"
}'
```
</details>
