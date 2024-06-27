import requests
from utils import get_babelfy_url, get_spotlight_url
from constants import BABELFY_HEADER, SPOTLIGHT_HEADER
from threading import Thread

class EntityLinking:
    def __init__(self, entities: list[str] = []) -> None:
        self.map = {}
        
        n = len(entities)

        if n > 3:
            map = {}
            def get_entities_thread(entities: list[str] = [], map: dict = {}) -> None:
                for entity in entities:
                    map[entity] = [self.__get_resource_babelfy(entity),
                                   self.__get_resource_spotlight(entity)]
            
            size_to_thread = n//3
            entities_thread_1 = entities[0:size_to_thread]
            entities_thread_2 = entities[size_to_thread: 2*size_to_thread]
            entities_thread_3 = entities[2*size_to_thread: n]

            t1 = Thread(target=get_entities_thread, args=(entities_thread_1, map))
            t2 = Thread(target=get_entities_thread, args=(entities_thread_2, map))
            t3 = Thread(target=get_entities_thread, args=(entities_thread_3, map))

            t1.start()
            t2.start()
            t3.start()

            t1.join()
            t2.join()
            t3.join()

            self.map = map
        else:
            for entity in entities:
                self.map[entity] = [self.__get_resource_babelfy(entity),
                                    self.__get_resource_spotlight(entity)]

    def get_linked_entities(self,) -> dict:
        return self.map
    
    def get_linked_relations(self, ) -> dict:
        return self.map
    
    def __get_resource_babelfy(self, entity: str) -> str:
        headers = BABELFY_HEADER
        response = requests.get(get_babelfy_url(entity),
                                headers=headers)

        if (response.status_code == 200):
            data = response.json()
            best_resource = max(data,
                                key=lambda resource: resource['score'])['DBpediaURL'] if data != [] else ''

            return best_resource
        
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
