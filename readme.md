PI_01_Data_Engineer-EDA-ETL-DOCKER-FastAPI-
_ PROYECTO INDIVIDUAL Nº1 para Henry_ Diciembre 2022 _ Data Engineering

Este es un proyecto trabaja sobre archivos en csv y json, luego se hace un EDA y ETL (solo a los fines de este proyecto), para luego levantarlo con docker en una API hecha por fastAPI.

Prologo
Hola! Me llamo Pablo Castro y en esta oportunidad estoy realizando este proyecto, como parte de los laboratorios de Henry donde he realizado un Bootcamp de 6 módulos intensivos.

Objetivo de trabajo
1. Ingesta de datos desde diversas fuentes.
2. Aplicar transformaciones que se consideren pertinentes.
3. Disponibilizar los datos limpios para su consulta a través de una API. Esta API estara construida en un entorno virtual dockerizado.

Las consultas a realizar son:

Máxima duración según tipo de film (película/serie), por plataforma y por año:

El request debe ser: get_max_duration(año, plataforma, [min o season])

Cantidad de películas y series (separado) por plataforma

El request debe ser: get_count_plataform(plataforma)

Cantidad de veces que se repite un género y plataforma con mayor frecuencia del mismo.

El request debe ser: get_listedin('genero')

Como ejemplo de género pueden usar 'comedy', el cuál deberia devolverles un cunt de 2099 para la plataforma de amazon.


Herramientas utilizadas:
    - Python
    - Pandas
    - Docker
    - FastAPI

Material consultado
https://hub.docker.com/r/tiangolo/uvicorn-gunicorn-fastapi/
https://github.com/tiangolo/uvicorn-gunicorn-fastapi-docker
https://fastapi.tiangolo.com/tutorial/
https://joserzapata.github.io/courses/python-ciencia-datos/pandas/