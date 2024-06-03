from DataLayer.Annotate import Annotate
from KnowledgeExtractionLayer.Extraction import Extraction
from dotenv import load_dotenv
import os

def main() -> None:
    load_dotenv('.env')
    corenlp_dir = os.environ.get('CORENLP_HOME', 'corenlp')
    
    ann = Annotate('Michael Jordan played basket', corenlp_dir)
    eel = Extraction(ann.doc)

    # Data Layer
    ann.display_tokens_and_labels()
    ann.display_dependency_tree()

    # Knowledge Extracion Layer
    eel.display_entities()
    eel.display_relations()

    print("\n")
    print("***************************************************************************************************************************************************")
    print("Example 2")
    print("***************************************************************************************************************************************************")
    print("\n")

    
    ann = Annotate("The quick brown fox called Manuel, which was being chased by a cunning and agile hound, jumped over the lazy dog lying near the barn.", corenlp_dir)
    eel = Extraction(ann.doc)

    # Data Layer
    ann.display_tokens_and_labels()
    ann.display_dependency_tree()

    # Knowledge Extracion Layer
    eel.display_entities()
    eel.display_relations()

if __name__=="__main__":
    main()