from DataLayer.Annotate import Annotate
from KnowledgeExtractionLayer.Extraction import Extraction
from dotenv import load_dotenv
import os

def main() -> None:
    load_dotenv('.env')
    corenlp_dir = os.environ.get('CORENLP_HOME', 'corenlp')
    
    ann = Annotate("""Berlin is the capital and largest city of Germany by both area and population. 
                      Its 3,769,495 inhabitants as of 31 December 2019 make it the most-populous city of the European Union, according to population within city limits. 
                      The city is also one of Germany's 16 federal states. 
                      It is surrounded by the state of Brandenburg, and contiguous with Potsdam, Brandenburg's capital. 
                      The two cities are at the center of the Berlin-Brandenburg capital region, which is, with about six million 
                      inhabitants and an area of more than 30,000 km2, Germany's third-largest metropolitan region after the Rhine-Ruhr and Rhine-Main regions. 
                      Berlin straddles the banks of the River Spree, which flows into the River Havel (a tributary of the River Elbe) in 
                      the western borough of Spandau. Among the city's main topographical features are the many lakes in the western and 
                      southeastern boroughs formed by the Spree, Havel, and Dahme rivers (the largest of which is Lake Müggelsee). 
                      Due to its location in the European Plain, Berlin is influenced by a temperate seasonal climate. About one-third of the city's 
                      area is composed of forests, parks, gardens, rivers, canals and lakes""", corenlp_dir)
    
    eel = Extraction(ann.doc)

    # Data Layer
    ann.display_tokens_and_labels()
    ann.display_dependency_tree()

    # Knowledge Extracion Layer
    eel.display_entities()
    eel.display_relations()

if __name__=="__main__":
    main()