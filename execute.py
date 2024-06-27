from DataLayer.Annotate import Annotate
from KnowledgeExtractionLayer.Extraction import Extraction
from dotenv import load_dotenv
import os
import sys
import signal
from RepresentationLayer.RDF_Generator import rdf_generator

def main() -> None:
    
    load_dotenv('.env')
    corenlp_dir = os.environ.get('CORENLP_HOME', 'corenlp')
    
    ann = Annotate("""Michael Jordan played basket""", corenlp_dir)
    ex = Extraction(ann.doc, ann.get_tokens_as_dict())
    for i in ex.relations:
        rdf_generator(i)



if __name__=="__main__":
    main()