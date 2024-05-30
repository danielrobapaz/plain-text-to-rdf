SETUP_USAGE_MESSAGE = '''Usage: python setup.py -d|--dir path_to_download_model
                       -l|--language model_language'''
SETUP_REPEATED_FLAGS = 'Flags can\'t be repeated, please check usage \n' + SETUP_USAGE_MESSAGE
SETUP_FLAGS = ['-d', '--dir', '-l', '--language']
UNEXISTING_FLAG_MESSAGE_ERROR = 'Flag doesn\'t exists'

CORENLP_VERSION='main'

BABELFY_HEADER = {
    'application': 'application/json'
}
BABELFY_API_URL='https://babelfy.io/v1/disambiguate?'
BABELFY_API_KEY='f9dcdcc4-2e98-4a64-bdfd-969af075e25b'

SPOTLIGHT_HEADER = {
    'accept': 'application/json'
}
SPOTLIGHT_API_URL='https://api.dbpedia-spotlight.org/en/annotate?'

DEPREL_DESCRIPTIONS = {
    "acl": "clausal modifier of noun (adjectival clause)",
    "advcl": "adverbial clause modifier",
    "advmod": "adverbial modifier",
    "amod": "adjectival modifier",
    "appos": "appositional modifier",
    "aux": "auxiliary",
    "case": "case marking",
    "cc": "coordinating conjunction",
    "ccomp": "clausal complement",
    "clf": "classifier",
    "compound": "compound",
    "conj": "conjunct",
    "cop": "copula",
    "csubj": "clausal subject",
    "dep": "unclassified dependent",
    "det": "determiner",
    "discourse": "discourse element",
    "dislocated": "dislocated elements",
    "expl": "expletive",
    "fixed": "fixed multiword expression",
    "flat": "flat multiword expression",
    "goeswith": "goes with",
    "iobj": "indirect object",
    "list": "list",
    "mark": "marker",
    "nmod": "nominal modifier",
    "nsubj": "nominal subject",
    "nummod": "numeric modifier",
    "obj": "object",
    "obl": "oblique nominal",
    "orphan": "orphan",
    "parataxis": "parataxis",
    "punct": "punctuation",
    "reparandum": "overridden disfluency",
    "root": "root",
    "vocative": "vocative",
    "xcomp": "open clausal complement"
}