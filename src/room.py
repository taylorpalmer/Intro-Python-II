# Implement a class to hold room information. This should have name and
# description attributes.
class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.n_to: Room = None
        self.s_to: Room = None
        self.e_to: Room = None
        self.w_to: Room = None

# 1) Adding these as attributes in the constructor is optional;
# in python you can arbitrarily set attributes on instances
# 2) the `: Room` syntax is a typehint. It just serves as a reminder
# for other developers that self.n_to is storing a Room object (as opposed to a str)
