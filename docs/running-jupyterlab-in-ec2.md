## Git pull

```
git clone https://github.com/vivasaayi/thulir.pygeo.git
cd  thulir.pygeo
```


## Build the Docker Image
> Note: We are not using DockerHub as of now. So build and run the image

```shell
make build
```

## Run the Jupyterlab

```shell
make jupyterlab 
```

## Access Juputerlab

Follow the instructions on the logs to access the Jupyterlab

## Install python packages

> Can this be done in docker composer step? We need to install the modules in the correct environment

```shell
pip install -r requirements.txt
```

## Run CLI

```shell
python ./geoparser/cli/cli.py landsat extract-tiles /data/landsat /data/landsat-tiles
python ./geoparser/cli/cli.py indices extract-ndvi /data/landsat /data/landsat-tiles
```