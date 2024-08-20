from enum import Enum


class TypedEnum(Enum):
    def __new__(cls, *args):
        obj = object.__new__(cls)
        obj._value_ = len(cls.__members__) + 1
        obj.id = obj._value_
        return obj

    @classmethod
    def by_name(cls, name):
        try:
            return next(member for member in cls if member.name == name)
        except StopIteration:
            raise ValueError(f"No {cls.__name__} member with name {name}")

    @classmethod
    def by_id(cls, id):
        try:
            return next(member for member in cls if member.id == id)
        except StopIteration:
            raise ValueError(f"No {cls.__name__} member with ID {id}")

    @classmethod
    def ids(cls):
        return [member.id for member in cls]

    @classmethod
    def names(cls):
        return [member.name for member in cls]
