from DataLayer.Annotate import Annotate
from KnowledgeExtractionLayer.Extraction import Extraction
from dotenv import load_dotenv
import os
import sys
import signal

def main() -> None:
    
    load_dotenv('.env')
    corenlp_dir = os.environ.get('CORENLP_HOME', 'corenlp')
    
    ann = Annotate("""Michael Jordan played basket""", corenlp_dir)

    tokens_dict = ann.get_tokens_as_dict()
    
    eel = Extraction(ann.doc)

    # Data Layer
    #ann.display_tokens_and_labels()
    #ann.display_dependency_tree()

    # Knowledge Extracion Laye
    eel.display_entities()
    eel.display_relations(tokens_dict)
    
def signal_handler(sig, frame):
    print("Corrida Terminada")
    exit(0)


if __name__=="__main__":
    main()
    signal.signal(signal.SIGINT, signal_handler)
    os.kill(os.getpid(), signal.SIGINT)