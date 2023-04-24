# snapp-challenge

For Deploy Application with Nginx run command :

````
git clone https://github.com/sdmoradi/snapp-challenge.git

cd snapp-challenge

docker compose up -d
````

For Deploy monitoring stack run command :

````
cd monitoring 

docker compose up -d
````

### Application address:

#### user: admin
#### password: password

- http://localhost
- http://localhost/v1/weather?city=tehran
- http://localhost/v1/weather?city=london

### Grafana address:

#### user: admin
#### password: admin

- http://localhost:3000

### Prometheus address:

- http://localhost:9090