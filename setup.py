import sys
from constants import SETUP_USAGE_MESSAGE, CORENLP_VERSION
from Exceptions import InvalidCommandLineUsage, UnexistingFlag
from ComandLineArguments import ComandLineArguments
from utils import write_env_file
import stanza

def main() -> None:
    try:
        arguments = sys.argv
        argument_parsers = ComandLineArguments(arguments)

        if not argument_parsers.is_valid():
            raise InvalidCommandLineUsage(SETUP_USAGE_MESSAGE)

        path_to_core_nlp = argument_parsers.get_value('-d', '--dir')
        choosen_language = argument_parsers.get_value('-l', '--language')
        

        write_env_file(core_nlp_path=path_to_core_nlp,
                       language=choosen_language)
        
        stanza.install_corenlp(dir=path_to_core_nlp)
        stanza.download_corenlp_models(dir=path_to_core_nlp, 
                                       model=choosen_language,
                                       version=CORENLP_VERSION)

    except InvalidCommandLineUsage as e:
        print(e.message)

    except UnexistingFlag as e:
        print(e.message)

if __name__ == "__main__":
    main()