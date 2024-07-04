# Convecsion de texto plano a RDF utilizando NLP.

Autores:
- Daniel Robayo, 18-11086@usb.ve
- Gabriel Chaurio, 17-10126@usb.ve
## Descripcion.
El proyecto consistio en implementar el sistema propuesto en (paper).

## Sobre la implementacion.

El sistema se desarrollo utilizando *python version 3.11* y se utilizaron las siguientes librerias.

El modelo de procesamiento de lenguaje escogido fue el *Standfor Core NLP*.

Para acceder el modelo utilizamos la libreria stanza la cual ofrece un *pipeline* y un servidor sobre el cual se pueden hacer *requests* para obtener anotaciones, entidades, etc...

## Ejecucion.

- Antes de ejecutar el sistema por primera vez hay que activar el entorno virtual e instalarle las librerias necesarias 
```
// crear el entorno virtual
python -m venv /path/to/venv

// activar el entorno virtual
source /path/to/env/bin/activate // linux

.venv\Scripts\activate.bat // windows
```

- Configurar el modelo Core NLP para stanza. En este paso se necesita descargar el modelo por lo que puede tomar un tiempo.
```
python setup.py  -d|--dir path_to_download_model -l|--language model_language
```

- Ejecutar execute junto con la direccion del archivo en donde se encuentra el texto a transformar.
```
python execute.py -f|--file path_to_txt
```

# Implementacion.
## Preprocesamiento.
Se encarga de anotar el texto de entrada. Estas anotaciones son utilizadas posteriormente. Se utilizo el *pipeline* que ofrece stanza.

Para cada *token* que se identifica, se obtienen las siguientes caracteristicas

-
-
-
-

## Extraccion de conocimiento.
En esta parte se extraen las entidades y relaciones. Se utilizo el servidor de CoreNLP para obtener las relaciones. Para vincular las entidades y relaciones se utilizaron las APIs the *dbpedia-spotlight* y *babelfy*. 

## Representacion.
Se utilizo la libreria rdflib para generar el rdf en formato XML.