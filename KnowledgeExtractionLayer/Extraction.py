from stanza import Document
from constants import DEPREL_DESCRIPTIONS
from . import EntityLinking

class Extraction:
    def __init__(self, 
                 tokenized_doc: Document) -> None:
        self.doc = tokenized_doc
        self.deprel_descriptions = DEPREL_DESCRIPTIONS

    def extract_relations(self) -> None:
        relations = []
        for sentence in self.doc.sentences:
            for word in sentence.words:
                if word.head != 0:
                    head = sentence.words[word.head - 1]
                    relation = {
                        "head": head.text,
                        "head_id": head.id,
                        "tail": word.text,
                        "tail_id": word.id,
                        "relation": word.deprel,
                        "relation_description": self.deprel_descriptions.get(word.deprel, "unknown")
                    }
                    relations.append(relation)
        return relations

    def extract_entities(self) -> None:
        doc_entities = self.doc.entities
        entities = [e.text  for e in doc_entities]
        
        el = EntityLinking.EntityLinking(entities)
        return el.get_linked_entities()
    
    def display_entities(self) -> None:
        print('\nEntidades')
        entities = self.extract_entities()

        print(f"\nNumero de Entidades: {len(entities)}")

        for entity in entities:
            print(f"Entity: {entity} | URIs: {entities[entity]}")
    
    def display_relations(self) -> None:
        print('\nRelaciones')
        relations = self.extract_relations()

        print(f"\nNumero de Relaciones: {len(relations)}")

        for rel in relations:
            print(f"Head (Token #{rel['head_id']}): {rel['head']} -> Tail (Token #{rel['tail_id']}): {rel['tail']} (Relation: {rel['relation_description']} [])")

    # Pendiente hayar tripleta. Si es verbo, encontrar quien apunta al verbo y a quien apunta el verbo (trippleta fromada). Encontrar la maanera de relacionar adjetivos a los sujetos o verbos (encontrar conector?)
    # Investigar aquellos que tienen : en la relacion con dos deprel.
