from operator import add, sub, mul, truediv


def connector(name=None):
    def set_value(source, val):
        nonlocal informant
        if connector["val"] is None:
            informant, connector["val"] = source, val
            if name is not None:
                print(f"{name} = {val}")
            inform_all_except(source, "new_val", constraints)
        else:
            if val != connector["val"]:
                print(f"Contradition detected: {val} vs {connector['val']}")

    def forget_value(source):
        nonlocal informant
        if source == informant:
            informant, connector["val"] = None, None
            if name is not None:
                print(f"{name} is forgotten")
            inform_all_except(source, "forget", constraints)

    informant = None
    constraints = []

    connector = {
        "val": None,
        "set_val": set_value,
        "forget": forget_value,
        "has_val": lambda: connector["val"] is not None,
        "connect": lambda source: constraints.append(source)
    }
    return connector


def inform_all_except(source, message, constraints):
    for c in constraints:
        if c != source:
            c[message]()


def converter(c, f):
    w, u, v, x, y = [connector() for _ in range(5)]
    multiplier(c, w, u)
    multiplier(v, x, u)
    adder(v, y, f)
    constant(w, 9)
    constant(x, 5)
    constant(y, 32)


def make_tenary_constraint(a, b, c, ab, ca, cb):
    def new_value():
        av, bv, cv = [connector["has_val"]() for connector in (a, b, c)]
        if av and bv:
            c["set_val"](constraint, ab(a["val"], b["val"]))
        elif cv and av:
            b["set_val"](constraint, ca(c["val"], a["val"]))
        elif cv and bv:
            a["set_val"](constraint, cb(c["val"], b["val"]))

    def forget_value():
        for connector in (a, b, c):
            connector["forget"](constraint)

    constraint = {"new_val": new_value, "forget": forget_value}
    for connector in (a, b, c):
        connector["connect"](constraint)
    return constraint


def multiplier(a, b, c):
    # a * b = c
    return make_tenary_constraint(a, b, c, mul, truediv, truediv)


def adder(a, b, c):
    # a + b = c
    return make_tenary_constraint(a, b, c, add, sub, sub)


def constant(a, num):
    constraint = {}
    a["set_val"](constraint, num)
    return constraint
