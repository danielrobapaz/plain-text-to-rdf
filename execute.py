from DataLayer.Annotate import Annotate
from KnowledgeExtractionLayer.Extraction import Extraction
from dotenv import load_dotenv
import os

def main() -> None:
    load_dotenv('.env')
    corenlp_dir = os.environ.get('CORENLP_HOME', 'corenlp')
    
    ann = Annotate('Michael Jordan played basket', corenlp_dir)
    eel = Extraction(ann.doc)

    ann.display_tokens_and_labels()
    ann.display_dependency_tree()

    eel.display_relations()

    print(eel.extract_entities())

if __name__=="__main__":
    main()