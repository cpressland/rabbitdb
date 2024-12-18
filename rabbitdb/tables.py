from piccolo.columns import Boolean, Date, ForeignKey, Text, Varchar
from piccolo.columns.readable import Readable
from piccolo.table import Table
from piccolo_admin.endpoints import TableConfig

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
    date_of_birth = Date()
    notes = Text()
    spayed_neutered = Boolean(default=False)

    @classmethod
    def get_readable(cls) -> Readable:
        return Readable(template="%s", columns=[cls.name])


rabbit = TableConfig(
    table_class=Rabbit,
    rich_text_columns=[Rabbit.notes],
    # link_column=Rabbit.name,
)


class HutchRabbit(Table, tablename="hutch_rabbits"):
    hutch = ForeignKey(references=Hutch)
    rabbit = ForeignKey(references=Rabbit, unique=True)


class RabbitFriend(Table, tablename="rabbit_friends"):
    rabbit = ForeignKey(references=Rabbit)
    friend = ForeignKey(references=Rabbit)
    are_friends = Boolean(default=True)
    # group_constraints = UniqueConstraint(["rabbit", "friend"]) // UniqueConstraint are coming in https://github.com/piccolo-orm/piccolo/pull/984


class Vaccinations(Table, tablename="vaccinations"):
    rabbit = ForeignKey(references=Rabbit)
    vaccination = ForeignKey(references=Vaccine)
    date = Date()
    expires = Date()
    notes = Text()
