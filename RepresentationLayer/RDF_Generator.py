from RepresentationLayer.DataOrdering import DataOrdering
from RepresentationLayer.Tripletes import Tripletes

from rdflib import Graph, Literal, RDF, URIRef
from rdflib.namespace import FOAF, XSD

class RDF_Generator:
    def __init__(self, data_ordering: DataOrdering, rel_dict: dict, ent_dict: dict) -> None:
        self.rel_dict = rel_dict
        self.ent_dict = ent_dict
        for (index, triplete) in enumerate(data_ordering.get_tripletes()):
            self.rdf_generator(triplete,index)
    
    def rdf_generator(self, tripletas: Tripletes, index = int):
    
        g = Graph()

        try:
            self.ent_dict[tripletas.subject]
            subject = URIRef(self.ent_dict[tripletas.subject][0])
        except:
            return print("No hay una URI asociada a la entidad, RDF no creado.")
        try:
            self.rel_dict[tripletas.predicate]
            relation = URIRef(self.rel_dict[tripletas.predicate][0])
        except:
            return print("No hay una URI asociada a la relacion/predicado, RDF no creado.")
        try:
            self.ent_dict[tripletas.object]
            object_ = URIRef(self.ent_dict[tripletas.object][0])
        except:
            object_ = Literal(tripletas.object)


        g.add((subject, relation, object_))
            
        g.serialize(destination=f'{index}.rdf', format='xml')

        print("Archivo RDF creado con éxito")