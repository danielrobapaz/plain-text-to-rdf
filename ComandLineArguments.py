from Exceptions import *
from constants import *
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
        not_empty_arguments = self.argument_map != {}
        complete_arguments = len(self.arguments[1:]) % 2 == 0 # every flag comes with a value
        keys_are_flags = all(key[0]=='-' or key[0:2] == '--' for key in self.argument_map) 
        flags_are_present = all(any(key == flag for flag in SETUP_FLAGS) for key in self.argument_map)
        
        return not_empty_arguments and complete_arguments and keys_are_flags and flags_are_present
    

    def get_value(self, flag: str, aux_flag: str) -> str:
        if not flag in self.argument_map and not aux_flag in self.argument_map:
            raise UnexistingFlag(UNEXISTING_FLAG_MESSAGE_ERROR)
        
        value = self.argument_map.get(flag, None)
        if not value:
            value = self.argument_map.get(aux_flag, None)
        
        return value
