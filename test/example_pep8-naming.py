import os as OS  # N812
from os import O_RDONLY as readonly  # N811


class sholud_use_cap_words_convention:  # N801

    def SHOULD_BE_LOWERCASE():  # N802
        OS
        readonly

    @classmethod
    def class_method(SHOULD_BE_LOWERCASE_AND_NAMED_CLS):  # N804, N803
        pass

    def method(should_be_named_self):  # N805
        SHOULD_BE_LOWERCASE = ''  # N806
        SHOULD_BE_LOWERCASE


def __should_not_start_and_end_with__():  # N807
    pass


class TestClass:
    shouldNotBeMixedCase = ''  # N815


shouldNotBeMixedCase = ''  # N816

# N801 class names should use CapWords convention
# N802 function name should be lowercase
# N803 argument name should be lowercase
# N804 first argument of a classmethod should be named 'cls'
# N805 first argument of a method should be named 'self'
# N806 variable in function should be lowercase
# N807 function name should not start and end with '__'
# N811 constant imported as non constant
# N812 lowercase imported as non-lowercase
# N813 camelcase imported as lowercase
# N814 camelcase imported as constant
# N815 mixedCase variable in class scope
# N816 mixedCase variable in global scope
# N817 camelcase imported as acronym
# N818 error suffix in exception names
