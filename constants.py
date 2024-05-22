SETUP_USAGE_MESSAGE = '''Usage: python setup.py -d|--dir path_to_download_model
                       -l|--language model_language'''
SETUP_REPEATED_FLAGS = 'Flags can\'t be repeated, please check usage \n' + SETUP_USAGE_MESSAGE
SETUP_FLAGS = ['-d', '--dir', '-l', '--language']
UNEXISTING_FLAG_MESSAGE_ERROR = 'Flag doesn\'t exists'

CORENLP_VERSION='main'