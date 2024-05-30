import stanza
import os
from dotenv import load_dotenv
from pathlib import Path
from nltk.tree import Tree
import time


class Annotate:
    def __init__(self, 
                 text: str,
                 corenlp_dir: str) -> None:
        self.text = text
        self.corenlp_dir = corenlp_dir
        
        self._setup_pipeline()

        self.__process_text()

    def _setup_pipeline(self) -> None:
        self.nlp = stanza.Pipeline('en')

    def __process_text(self) -> None:
        start_time = time.time()
        self.doc = self.nlp(self.text)
        end_time = time.time()
        print(f"Texto Procesado. Tiempo para procesar el texto: {end_time - start_time:.4f} segundos")

    def get_tokens_as_dict(self) -> None:
        tokens_dict = {}
        for sentence in self.doc.sentences:
            for token in sentence.tokens:
                tokens_dict[token.text] = {
                    'lemma': [word.lemma for word in token.words],
                    'pos': [word.pos for word in token.words],
                    'xpos': [word.xpos for word in token.words],
                    'head': [word.head for word in token.words],
                    'deprel': [word.deprel for word in token.words]
                }
        return tokens_dict

    def get_tokens_as_list(self) -> None:
        tokens_list = []
        for sentence in self.doc.sentences:
            for token in sentence.tokens:
                for word in token.words:
                    token_info = {
                        'id': word.id,
                        'text': token.text,
                        'lemma': word.lemma,
                        'pos': word.pos,
                        'xpos': word.xpos,
                        'head': word.head,
                        'deprel': word.deprel
                    }
                    tokens_list.append(token_info)
        return tokens_list

    def display_tokens_and_labels(self) -> None:
        print("\nTokens y Etiquetas:")
        start_time = time.time()
        
        for sentence in self.doc.sentences:
            for token in sentence.tokens:
                for word in token.words:
                    print(f"Token #{word.id}: {token.text}")
                    print(f"  Lemma: {word.lemma}")    
                    print(f"  POS: {word.pos}")       
                    print(f"  XPOS: {word.xpos}")      
                    print(f"  Head: {word.head}")       
                    print(f"  Deprel: {word.deprel}\n")    

        end_time = time.time()
        print(f"Tiempo para extraer y mostrar tokens y etiquetas: {end_time - start_time:.4f} segundos\n")

    def to_nltk_tree(self, node: Tree) -> Tree:
        if node.deprel == 'root':
            return Tree(node.text, [self.to_nltk_tree(child) for child in self.doc.sentences[0].words if child.head == node.id])
        else:
            return Tree(f'{node.text} ({node.deprel})', [self.to_nltk_tree(child) for child in self.doc.sentences[0].words if child.head == node.id])

    def display_dependency_tree(self) -> None:
        print("Arbol de Dependencias:\n")
        start_time = time.time()
        
        for sentence in self.doc.sentences:
            root = [word for word in sentence.words if word.head == 0][0]
            tree = self.to_nltk_tree(root)
            tree.pretty_print()
        
        end_time = time.time()
        print(f"\nTiempo para convertir a arbol: {end_time - start_time:.4f} segundos")