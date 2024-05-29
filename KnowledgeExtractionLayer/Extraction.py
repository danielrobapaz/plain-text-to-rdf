import stanza
import os
from dotenv import load_dotenv
from pathlib import Path
from nltk.tree import Tree
import time

class RelationDetectionLayer:
    def __init__(self, tokenized_doc):
        self.doc = tokenized_doc
        self.deprel_descriptions = {
            "acl": "clausal modifier of noun (adjectival clause)",
            "advcl": "adverbial clause modifier",
            "advmod": "adverbial modifier",
            "amod": "adjectival modifier",
            "appos": "appositional modifier",
            "aux": "auxiliary",
            "case": "case marking",
            "cc": "coordinating conjunction",
            "ccomp": "clausal complement",
            "clf": "classifier",
            "compound": "compound",
            "conj": "conjunct",
            "cop": "copula",
            "csubj": "clausal subject",
            "dep": "unclassified dependent",
            "det": "determiner",
            "discourse": "discourse element",
            "dislocated": "dislocated elements",
            "expl": "expletive",
            "fixed": "fixed multiword expression",
            "flat": "flat multiword expression",
            "goeswith": "goes with",
            "iobj": "indirect object",
            "list": "list",
            "mark": "marker",
            "nmod": "nominal modifier",
            "nsubj": "nominal subject",
            "nummod": "numeric modifier",
            "obj": "object",
            "obl": "oblique nominal",
            "orphan": "orphan",
            "parataxis": "parataxis",
            "punct": "punctuation",
            "reparandum": "overridden disfluency",
            "root": "root",
            "vocative": "vocative",
            "xcomp": "open clausal complement"
        }

    def extract_relations(self):
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

    def display_relations(self):
        relations = self.extract_relations()
        for rel in relations:
            print(f"Head (Token #{rel['head_id']}): {rel['head']} -> Tail (Token #{rel['tail_id']}): {rel['tail']} (Relation: {rel['relation_description']} [])")

    # Pendiente hayar tripleta. Si es verbo, encontrar quien apunta al verbo y a quien apunta el verbo (trippleta fromada). Encontrar la maanera de relacionar adjetivos a los sujetos o verbos (encontrar conector?)
    # Investigar aquellos que tienen : en la relacion con dos deprel.
