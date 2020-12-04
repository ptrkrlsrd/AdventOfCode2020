import shlex
from typing import List
from schema import Schema, And, Use, Optional, SchemaError

def check(schema: Schema, data, debug=False):
    try:
        schema.validate(data)
        return True
    except SchemaError as e:
        if debug:
            print(e)
        return False

if __name__ == "__main__":
    validation_schema = Schema({
            'byr': And(Use(str)),
            'iyr': And(Use(str)),
            'eyr': And(Use(str)),
            'hgt': And(Use(str)),
            'hcl': And(Use(str)),
            'ecl': And(Use(str)),
            'pid': And(Use(str)),
            Optional('cid'): And(Use(str))
    })

    valid_passports: int = 0

    with open("./data/input.txt") as f:
        content: str = f.read()
        passports: List[str] = content.split("\n\n")

        for line in passports:
            passport = dict(token.split(':') for token in shlex.split(line))
            if check(validation_schema, passport):
                valid_passports += 1

    print("{}".format(valid_passports))
