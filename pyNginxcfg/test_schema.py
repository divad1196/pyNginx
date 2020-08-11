from schema import Schema, And, Or, Use, Optional


def test(schem):
    # Valide if
    a.validate({1: 4})
    print("OK1")
    a.validate({1: 4, 2: 5})
    print("OK2")
    a.validate({1: 4, 3: 6})
    print("OK3")
    a.validate({2: 5, 3: 6})
    print("OK4")
    a.validate({1: 4, 2: 5, 3: 6})
    print("OK5")
    # Not valid if
    try:
        a.validate({2: 5})
    except Exception as e:
        print("OK6")
    try:
        a.validate({3: 6})
    except Exception as e:
        print("OK7")


a = Schema(
    Or(
        {1: int, Optional(2): int, Optional(3): int},
        {2: int, 3: int}
    )
)

test(a)

# def haskey(key):
#     return lambda d: isinstance(d, dict) and key in d

def haskey(key):
    return Schema(lambda d: isinstance(d, dict) and key in d, name="has key {key}".format(key=key))


b = Schema(And(
    {
        "test": int, 
        Optional(1): int,
        Optional(2): int,
        Optional(3): int,
    },
    Or(
        haskey(1),
        And(
            haskey(2),
            haskey(3)
        )
    )
))
b.validate({"test": 54, 1: 4, 2: 5, 3: 6})

from schema import Hook
def _my_function(key, scope, error):
    print(key, scope, error)

Hook("key", handler=_my_function)
