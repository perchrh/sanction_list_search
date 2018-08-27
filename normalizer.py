import unicodedata
from dataobjects import NameAlias


def normalize_aliases(name_aliases: list):
    all_name_parts = set()
    for name_alias in name_aliases:
        normalized_name_alias = normalize_name_alias(name_alias)
        for value in normalized_name_alias:
            all_name_parts.add(value)

    return all_name_parts


import functools


def normalize_name_alias(name_alias: NameAlias):
    all_name_parts = set()
    for name_part in name_alias.name_parts:


        name_part_value = name_part.part
        split_characters = [x for x in name_part_value if not x.isalpha() and not x.isdigit()]
        if split_characters:
            name_part_value = functools.reduce(lambda s, sep: s.replace(sep, ' '), split_characters, name_part_value).strip()
            for name_part_part in name_part_value.split():
                normalized_name = normalize_word(name_part_part)
                all_name_parts.add(normalized_name)
        else:
            normalized_name = normalize_word(name_part_value)
            all_name_parts.add(normalized_name)
    return all_name_parts


def normalize_word(word: str):
    return replace_nordic_letters(remove_diacritics(word.lower()))


def replace_nordic_letters(word: str):
    return word.replace("ø", "o").replace("æ", "ae").replace("å", "aa").replace("ä", "a").replace("ö", "o")


def remove_diacritics(word: str):
    return ''.join(c for c in unicodedata.normalize('NFKD', word) if unicodedata.category(c) != 'Mn')
