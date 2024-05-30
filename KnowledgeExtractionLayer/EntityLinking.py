import requests
from utils import get_babelfy_url, get_spotlight_url
from constants import BABELFY_HEADER, SPOTLIGHT_HEADER


class EntityLinking:
    def __init__(self, entities: list[str] = ['']) -> None:
        self.map = {}
        for entity in entities:
            self.map[entity] = [self.__get_resource_babelfy(entity),
                                self.__get_resource_spotlight(entity)]
            
    
    def get_linked_entities(self, ) -> dict:
        return self.map
    
    def __get_resource_babelfy(self, entity: str) -> str:
        headers = BABELFY_HEADER
        response = requests.get(get_babelfy_url(entity),
                                headers=headers)

        if (response.status_code == 200):
            data = response.json()
            best_resource = max(data,
                                key=lambda resource: resource['score'])

            return best_resource['DBpediaURL']
        
        return None

    def __get_resource_spotlight(self, entity: str) -> str:
        headers = SPOTLIGHT_HEADER
        response = requests.get(get_spotlight_url(entity),
                                headers=headers)
        
        if (response.status_code == 200):
            data = response.json()
            resource = data.get('Resource')

            if resource:
                return resource['@URI']
        return None
    
el = EntityLinking(['Bank', 'Fox', 'Michael_jordan'])
print(el.get_linked_entities())
