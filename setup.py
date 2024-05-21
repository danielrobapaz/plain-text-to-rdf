import sys
from constants import SETUP_USAGE_MESSAGE, SETUP_FLAGS, SETUP_REPEATED_FLAGS
from Exceptions import InvalidCommandLineUsage
from utils import get_list_safe
    
class ComandLineArguments:
    def __init__(self, arguments: str) -> None:
        self.arguments = arguments
        self.__create_argument_map()

    def __create_argument_map(self) -> str:
        argument_map = {}
        for i in range(1, len(self.arguments[1:]), 2):
            if self.arguments[i] in argument_map:
                raise InvalidCommandLineUsage(SETUP_REPEATED_FLAGS)
            
            argument_map[self.arguments[i]] = get_list_safe(self.arguments, i+1, None)

        self.argument_map = argument_map

    def is_valid(self) -> bool:
        complete_arguments = len(self.arguments[1:]) % 2 == 0 # every flag comes with a value
        keys_are_flags = all(key[0]=='-' or key[0:2] == '--' for key in self.argument_map) 
        flags_are_present = all(any(key == flag for flag in SETUP_FLAGS)for key in self.argument_map)
        
        return complete_arguments and keys_are_flags and flags_are_present


def main() -> None:
    try:
        arguments = sys.argv
        argument_parsers = ComandLineArguments(arguments)

        if not argument_parsers.is_valid():
            raise InvalidCommandLineUsage(SETUP_USAGE_MESSAGE)
        
    except InvalidCommandLineUsage as e:
        print(e.message)

if __name__ == "__main__":
    main()