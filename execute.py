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

    print(tokens_dict)



if __name__=="__main__":
    main()