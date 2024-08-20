
# How to run the code

step 1: Clone the repository

```bash
git clone https://github.com/holys/flask-boilerplate.git
```

step 2: Change the directory

```bash
cd flask-boilerplate
```

step 3: Build docker image

```bash
docker build -t flask-boilerplate .
```

step 4: Run the docker container via docker-compose

```bash
docker-compose up
``` 

step 5: test the api 
```bash
curl http://localhost:6000/example

# output
{
    "id": "1",
    "name": "example"
}
```
