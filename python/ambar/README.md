# Python Version: 3.4

### Manually

#### Install libs
```
$ pip install -r requirements.txt
```

#### Run app
```
$ FLASK_APP=app.py flask run
```
__

### Using docker

#### Build image
```
$ docker build -t ambar/dev:1.0 -f Dockefile .
```

#### Run image
```
$ docker run -d -p 5000:5000 ambar/dev:1.0
```

__

#### Usage
```
/cidades
$ curl -XGET "http://localhost:5000/cidade?id=3477"
$ curl -XGET "http://localhost:5000/cidade?id=3498"
$ curl -XGET "http://localhost:5000/cidade?id=3476"

/analise
$ curl -XGET "http://localhost:5000/analise?data_inicial=2019-03-01&data_final=2019-05-01"
```