from RepresentationLayer.DataOrdering import DataOrdering
from RepresentationLayer.Tripletes import Tripletes

from rdflib import Graph, Literal, RDF, URIRef
from rdflib.namespace import FOAF, XSD

class RDF_Generator:
    def __init__(self, data_ordering: DataOrdering, rel_dict: dict, ent_dict: dict, filename: str) -> None:
        self.rel_dict = rel_dict
        self.ent_dict = ent_dict
        self.filename = filename
        for (index, triplete) in enumerate(data_ordering.get_tripletes()):
            self.rdf_generator(triplete,index)

            
    
    def rdf_generator(self, tripletas: Tripletes, index = int):
    
        g = Graph()

        namespace = "http://example.org/"

        try:
            self.ent_dict[tripletas.subject]
            subject = URIRef(self.ent_dict[tripletas.subject][0])
        except:
            subject = URIRef(namespace + tripletas.subject.replace(" ", "_"))
        try:
            self.rel_dict[tripletas.predicate]
            relation = URIRef(self.rel_dict[tripletas.predicate][0])
        except:
            relation = URIRef(namespace + tripletas.predicate)
        try:
            self.ent_dict[tripletas.object]
            object_ = URIRef(self.ent_dict[tripletas.object][0])
        except:
            object_ = Literal(tripletas.object)


        if len(subject) > 0 and len(relation) > 0 and len(object_) > 0:
            g.add((subject, relation, object_))
            g.serialize(destination=f'./test/{self.filename}/{index}.rdf', format='xml')
            print("Archivo RDF creado con éxito")
        else:
            print(f"Some argument was empty, check for errors in text. Subject {subject}, Relation {relation}, Object {object_}")

        