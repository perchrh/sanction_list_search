class NameAlias:
    def __init__(self, name_parts: list = None, name_language: str = None, gender: str = None):
        self.name_parts = [n for n in name_parts if n.is_not_empty()]
        self.name_language = name_language
        self.gender = gender

    def __repr__(self):
        return ' '.join(str(x) for x in self.name_parts)


class NamePart:
    def __init__(self, part: str, is_firstname: bool = True):
        self.part = part.strip()
        self.is_firstname = is_firstname

    def is_not_empty(self):
        if self.part:
            return True
        else:
            return False

    def __repr__(self):
        return str(self.part)


class ListSubject:
    def __init__(self, namealiases: list, list_subject_ref):
        self.namealiases = namealiases
        self.list_subject_ref = list_subject_ref

    def __repr__(self):
        return self.namealiases
