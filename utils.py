from dotenv import load_dotenv

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

    load_dotenv('.env')