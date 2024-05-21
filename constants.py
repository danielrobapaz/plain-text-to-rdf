SETUP_USAGE_MESSAGE = '''Usage: python setup.py -f|--file path_to_download_model
                       -l|--language model_language'''
SETUP_REPEATED_FLAGS = 'Flags can\'t be repeated, please check usage \n' + SETUP_USAGE_MESSAGE
SETUP_FLAGS = ['-f', '--file', '-l', '--language']