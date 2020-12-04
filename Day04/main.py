import shlex
from schema import Schema, And, Use, Optional, SchemaError

def check(conf_schema, conf, debug=False):
    try:
        conf_schema.validate(conf)
        return True
    except SchemaError as e:
        if debug:
            print(e)
        return False

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

valid = 0

with open("./data/input.txt") as f:
    content = f.read()
    passports = content.split("\n\n")
    for line in passports:
        passport = dict(token.split(':') for token in shlex.split(line))
        if check(validation_schema, passport):
            valid += 1

print("{}".format(valid))
