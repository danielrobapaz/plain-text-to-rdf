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
        self.tokens_dict = {}
        
        self._setup_pipeline()

        self.__process_text()

        self.tokens_dict = self.get_tokens_as_dict()

        self.calculate_statistics()

    def _setup_pipeline(self) -> None:
        self.nlp = stanza.Pipeline(lang='en',verbose=False)

    def __process_text(self) -> None:
        start_time = time.time()
        self.doc = self.nlp(self.text)
        end_time = time.time()
        print(f"Texto Procesado. Tiempo para procesar el texto: {end_time - start_time:.4f} segundos")

    def get_tokens_as_dict(self) -> dict:
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

    def calculate_statistics(self) -> None:
        number_of_words = len(self.text.split(' '))
        number_of_tokens = len(set(self.tokens_dict.keys()))

        verbs = [token for token in self.tokens_dict
                 if self.tokens_dict[token]['pos'][0] == 'VERB']
        number_of_verbs = len(set(verbs))

        print('Estadisticas de las anotaciones: ')
        print(f'Cantidad de palabras: {number_of_words}')
        print(f'Cantidad de tokens: {number_of_tokens}')
        print(f'Cantidad de verbos: {number_of_verbs}')
        print('-------------------------')

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

        count = 0
        
        for sentence in self.doc.sentences:
            for token in sentence.tokens:
                for word in token.words:
                    count += 1
                    print(f"Token #{word.id}: {token.text}")
                    print(f"  Lemma: {word.lemma}")    
                    print(f"  POS: {word.pos}")       
                    print(f"  XPOS: {word.xpos}")      
                    print(f"  Head: {word.head}")       
                    print(f"  Deprel: {word.deprel}\n")    
        
        print(f"\nCantidad de Tokens = {count}")
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