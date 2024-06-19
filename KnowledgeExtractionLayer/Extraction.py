from stanza import Document
from constants import DEPREL_DESCRIPTIONS
from . import EntityLinking
from stanza.server import CoreNLPClient
import utils


class Extraction:
    def __init__(self, 
                 tokenized_doc: Document) -> None:
        self.doc = tokenized_doc
        self.relations = []
        self.entities = []
        self.deprel_descriptions = DEPREL_DESCRIPTIONS

    def extract_relations(self,tokens_dict) -> None:
        relations = []

        with CoreNLPClient(annotators=["openie"],
                           endpoint='http://localhost:9500',
                           be_quiet=True) as client:
            ann = client.annotate(self.doc.text)

            for sentence in ann.sentence:
                for triple in sentence.openieTriple:
                    relations.append(utils.map_triple_to_dict(triple,tokens_dict))

        self.relations = relations
        
        relations_to_link = [r['relation'] for r in relations]
        # el = EntityLinking.EntityLinking(relations_to_link)
        # self.relations_linking = el.get_linked_relations()


    def extract_entities(self) -> None:
        doc_entities = self.doc.entities
        entities = [e.text  for e in doc_entities]
        
        # el = EntityLinking.EntityLinking(entities)
        # self.entities = el.get_linked_entities()
    
    def display_entities(self) -> None:
        if self.entities == []:
            self.extract_entities()
        
        print('\nEntidades')

        print(f"\nNumero de Entidades: {len(self.entities)}")

        for entity in self.entities:
            print(f"Entity: {entity} | URIs: {self.entities[entity]}")
    
    def display_relations(self,tokens_dict) -> None:
        if self.relations == []:
            self.extract_relations(tokens_dict)
        print('\nRelaciones')

        print(f"\nNumero de Relaciones: {len(self.relations)}")

        print(self.relations)

        # print(self.relations_linking)
