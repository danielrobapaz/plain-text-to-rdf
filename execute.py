from DataLayer.Annotate import Annotate
from KnowledgeExtractionLayer.Extraction import Extraction
from RepresentationLayer.RDF_Generator import RDF_Generator
from RepresentationLayer.DataOrdering import DataOrdering
import nltk
from dotenv import load_dotenv
import os
from utils import kill_process_using_port
import sys
from ComandLineArguments import ComandLineArguments

def main() -> None:

    nltk.download('stopwords',quiet=True)

    kill_process_using_port(9500)

    load_dotenv('.env')
    corenlp_dir = os.environ.get('CORENLP_HOME', 'corenlp')
    
    test_folder = f'./test'

    arguments = sys.argv
    argument_parsers = ComandLineArguments(arguments)
        
    file_path = argument_parsers.get_value('-f', '--file')

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()
        file_real_name = file_path.split("/")[-1].replace('.txt', '')
        os.makedirs(f'./test/{file_real_name}', exist_ok=True)
    except:
        raise Exception("Invalid path. No file found.")

    ann = Annotate(text, corenlp_dir)
    ex = Extraction(ann.doc, ann.get_tokens_as_dict())
    ordering = DataOrdering(ex)
    RDF_Generator(ordering, ex.relations_linking, ex.entities, file_real_name)
    kill_process_using_port(9500)



if __name__=="__main__":
    main()