from rdflib import Graph, Literal, RDF, URIRef
from rdflib.namespace import FOAF, XSD

def rdf_generator(tripletas):
    
    g = Graph()

    namespace = "http://example.org/"
    
    # print(tripletas)

    subject = URIRef(namespace + tripletas['subject'].replace(" ", "_"))
    relation = URIRef(namespace + tripletas['relation'])
    object_ = Literal(tripletas['object'])
    g.add((subject, relation, object_))
        
    g.serialize(destination='tripletas.rdf', format='xml')

    print("Archivo RDF creado con éxito")