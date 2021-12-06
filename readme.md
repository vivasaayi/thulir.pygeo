# Docker

## InstallPackage
* Update the docker compose file 

## Build docker image

```
make build
```

## Run the applicaiton
```
make run
```


### Download files from S3 in bulk




# Run

```
docker build -t geo-parser_build .
docker run -it -p 12345:8888 -v ${PWD}:/src geo-parser_build
```