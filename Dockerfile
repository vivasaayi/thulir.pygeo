FROM osgeo/gdal

RUN apt-get update

RUN apt-get -y install python3-pip

RUN pip3 install scipy matplotlib jupyterlab

RUN pip3 list

EXPOSE 8888

CMD ["jupyter", "lab", "--allow-root", "--ip", "0.0.0.0"]