from RepresentationLayer.DataOrdering import DataOrdering
from RepresentationLayer.Tripletes import Tripletes

from rdflib import Graph, Literal, RDF, URIRef
from rdflib.namespace import FOAF, XSD

class RDF_Generator:
    def __init__(self, data_ordering: DataOrdering) -> None:
        for (index, triplete) in enumerate(data_ordering.get_tripletes()):
            self.rdf_generator(triplete, index)
    
    def rdf_generator(self,
                      triplete: Tripletes, 
                      index: int):
    
        g = Graph()

        namespace = "http://example.org/"

        subject = URIRef(namespace + triplete.subject.replace(" ", "_"))
        relation = URIRef(namespace + triplete.predicate)
        object_ = Literal(triplete.object)
        g.add((subject, relation, object_))
            
        g.serialize(destination=f'{index}.rdf', format='xml')

        print("Archivo RDF creado con éxito")