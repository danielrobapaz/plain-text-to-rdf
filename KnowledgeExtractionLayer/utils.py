import constants

def get_babelfy_url(text: str) -> str:
    return constants.BABELFY_API_URL + f"text={text}&lang=EN&key={constants.BABELFY_API_KEY}"

def get_spotlight_url(text: str) -> str:
    return constants.SPOTLIGHT_API_URL + f"text={text}"