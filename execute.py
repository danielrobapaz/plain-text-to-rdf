from DataLayer.Annotate import Annotate
from KnowledgeExtractionLayer.Extraction import Extraction
from RepresentationLayer.RDF_Generator import RDF_Generator
from RepresentationLayer.DataOrdering import DataOrdering

from dotenv import load_dotenv
import os

def main() -> None:
    
    load_dotenv('.env')
    corenlp_dir = os.environ.get('CORENLP_HOME', 'corenlp')
    
    test_folder = f'./test'
    

    for filename in os.listdir(test_folder):
        print(f'Archivo de texto: {filename}')
        if filename.endswith('.txt'):
            file_path = os.path.join(test_folder, filename)
            with open(file_path, 'r', encoding='utf-8') as file:
                text = file.read()
            file_real_name = filename.replace('.txt', '')
            os.makedirs(f'./test/{file_real_name}', exist_ok=True)

            ann = Annotate(text, corenlp_dir)
            ex = Extraction(ann.doc, ann.get_tokens_as_dict())
            ordering = DataOrdering(ex)
            RDF_Generator(ordering, ex.relations_linking, ex.entities, file_real_name)



if __name__=="__main__":
    main()