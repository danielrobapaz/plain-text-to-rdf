from DataLayer.Annotate import Annotate
from KnowledgeExtractionLayer.Extraction import Extraction
from RepresentationLayer.RDF_Generator import RDF_Generator
from RepresentationLayer.DataOrdering import DataOrdering

from dotenv import load_dotenv
import os

def main() -> None:
    
    load_dotenv('.env')
    corenlp_dir = os.environ.get('CORENLP_HOME', 'corenlp')
    
    ann = Annotate("""Leonardo Da Vinci painted the Monalisa""", corenlp_dir)
    ex = Extraction(ann.doc, ann.get_tokens_as_dict())
    ordering = DataOrdering(ex)
    rdf_generator = RDF_Generator(ordering)



if __name__=="__main__":
    main()