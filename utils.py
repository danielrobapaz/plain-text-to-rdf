from dotenv import load_dotenv
import psutil
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

def get_list_safe(l: list, index: int, default: any = None):
    try:
        return l[index]
    except:
        return default
    
def write_env_file(core_nlp_path: str,
                   language: str) -> None:
    f = open('.env', 'w')
    f.write(f'CORENLP_HOME={core_nlp_path}\n')
    f.write(f'MODEL_LANGUAGE={language}')
    f.close()

import constants

def get_babelfy_url(text: str) -> str:
    return constants.BABELFY_API_URL + f"text={text}&lang=EN&key={constants.BABELFY_API_KEY}"

def get_spotlight_url(text: str) -> str:
    return constants.SPOTLIGHT_API_URL + f"text={text}"

def map_triple_to_dict(triple,tokens_dict) -> dict:

    if len(triple.relation.split(" ")) > 1:
        filtered_relation = remove_stopwords(triple.relation)
    else:
        filtered_relation = triple.relation

    # If multiple values in filtered_relation, implement to choose only the verb... ? Error in file 4:
    # Traceback (most recent call last):
    # File "C:\Users\gabri\OneDrive\Documents\VMBoxShared\abr_jul_2024\Miniproyecto\plain-text-to-rdf\execute.py", line 40, in <module>
    #     main()
    # File "C:\Users\gabri\OneDrive\Documents\VMBoxShared\abr_jul_2024\Miniproyecto\plain-text-to-rdf\execute.py", line 32, in main
    #     ex = Extraction(ann.doc, ann.get_tokens_as_dict())
    #         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    # File "C:\Users\gabri\OneDrive\Documents\VMBoxShared\abr_jul_2024\Miniproyecto\plain-text-to-rdf\KnowledgeExtractionLayer\Extraction.py", line 17, in __init__
    #     self.extract_relations(tokens)
    # File "C:\Users\gabri\OneDrive\Documents\VMBoxShared\abr_jul_2024\Miniproyecto\plain-text-to-rdf\KnowledgeExtractionLayer\Extraction.py", line 34, in extract_relations
    #     relations.append(utils.map_triple_to_dict(triple, tokens_dict))
    #                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    # File "C:\Users\gabri\OneDrive\Documents\VMBoxShared\abr_jul_2024\Miniproyecto\plain-text-to-rdf\utils.py", line 36, in map_triple_to_dict
    #     'relation': tokens_dict[filtered_relation]["lemma"][0],
    #                 ~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
    # KeyError: 'charges toward'

    return {
        'subject': triple.subject,
        'relation': tokens_dict[filtered_relation]["lemma"][0],
        'object': triple.object
    }

def kill_process_using_port(port):
        for proc in psutil.process_iter(['pid', 'name', 'connections']):
            for conn in proc.info['connections']:
                if conn.laddr.port == port:
                    # print(f"Killing process {proc.info['pid']} ({proc.info['name']}) using port {port}")
                    proc.terminate()
                    proc.wait()  # Esperar a que el proceso termine
                    return True
                
def remove_stopwords(input_text):

    stop_words = set(stopwords.words('english'))
    words = input_text.split(" ")
    filtered_words = [word for word in words if word.lower() not in stop_words]
    filtered_text = ' '.join(filtered_words)
    return filtered_text