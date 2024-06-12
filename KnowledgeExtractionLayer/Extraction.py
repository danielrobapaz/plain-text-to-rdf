from stanza import Document
from constants import DEPREL_DESCRIPTIONS
from . import EntityLinking
from stanza.server import CoreNLPClient

class Extraction:
    def __init__(self, 
                 tokenized_doc: Document) -> None:
        self.doc = tokenized_doc
        self.relations = []
        self.entities = []
        self.deprel_descriptions = DEPREL_DESCRIPTIONS

    def extract_relations(self) -> None:
        relations = []

        with CoreNLPClient(annotators=["openie"],
                           endpoint='http://localhost:9156') as client:
            ann = client.annotate(self.doc.text)

            for sentence in ann.sentence:
                for triple in sentence.openieTriple:
                    relations.append(triple)

            self.relations = relations

    def extract_entities(self) -> None:
        doc_entities = self.doc.entities
        entities = [e.text  for e in doc_entities]
        
        el = EntityLinking.EntityLinking(entities)
        self.entities = el.get_linked_entities()
    
    def display_entities(self) -> None:
        if self.entities == []:
            self.extract_entities()
        
        print('\nEntidades')

        print(f"\nNumero de Entidades: {len(self.entities)}")

        for entity in self.entities:
            print(f"Entity: {entity} | URIs: {self.entities[entity]}")
    
    def display_relations(self) -> None:
        if self.relations == []:
            self.extract_relations()
        print('\nRelaciones')

        print(f"\nNumero de Relaciones: {len(self.relations)}")

        print(self.relations)