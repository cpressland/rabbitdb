from piccolo.columns import Boolean, Date, ForeignKey, Text, Varchar
from piccolo.columns.column_types import LazyTableReference
from piccolo.columns.m2m import M2M
from piccolo.columns.readable import Readable
from piccolo.table import Table

# Add Uploads for Vaccinations
# Add table for Vet Visits


class Hutch(Table, tablename="hutches"):
    name = Varchar(length=25)
    notes = Text()

    @classmethod
    def get_readable(cls) -> Readable:
        return Readable(template="%s", columns=[cls.name])


class Vaccine(Table, tablename="vaccines"):
    name = Varchar(length=50)
    notes = Text()

    @classmethod
    def get_readable(cls) -> Readable:
        return Readable(template="%s", columns=[cls.name])


class Rabbit(Table, tablename="rabbits"):
    name = Varchar(length=50)
    colour = Varchar(length=15)
    breed = Varchar(length=50)
    friends = M2M(LazyTableReference("RabbitFriends", module_path=__name__))
    hutch = M2M(LazyTableReference("RabbitHutch", module_path=__name__))
    date_of_birth = Date()
    notes = Text()
    spayed_neutered = Boolean(default=False)

    @classmethod
    def get_readable(cls) -> Readable:
        return Readable(template="%s", columns=[cls.name])


class RabbitFriends(Table, tablename="rabbit_friends"):
    rabbit = ForeignKey(references=Rabbit)
    friend = ForeignKey(references=Rabbit)


class RabbitHutch(Table, tablename="rabbit_hutches"):
    hutch = ForeignKey(references=Hutch)
    rabbit = ForeignKey(references=Rabbit, unique=True)


# class RabbitFriend(Table, tablename="rabbit_friends"):
#     rabbit = ForeignKey(references=Rabbit)
#     friend = ForeignKey(references=Rabbit)
#     are_friends = Boolean(default=True)
#     # group_constraints = UniqueConstraint(["rabbit", "friend"]) // UniqueConstraint are coming in https://github.com/piccolo-orm/piccolo/pull/984


class Vaccinations(Table, tablename="vaccinations"):
    rabbit = ForeignKey(references=Rabbit)
    vaccination = ForeignKey(references=Vaccine)
    date = Date()
    expires = Date()
    notes = Text()
