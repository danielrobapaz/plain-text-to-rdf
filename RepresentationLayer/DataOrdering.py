from KnowledgeExtractionLayer.Extraction import Extraction
from . import Tripletes

class DataOrdering:
    def __init__(self, extraction: Extraction) -> None:
        self.tripletes = []

        for r in extraction.relations:
            self.tripletes.append(Tripletes.Tripletes(
                                    r['subject'],
                                    r['relation'],
                                    r['object']))
        

    def get_tripletes(self) -> list[Tripletes.Tripletes]:
        return self.tripletes
            
        