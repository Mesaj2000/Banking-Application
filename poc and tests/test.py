class Animal(object):
    name = "[default name]"
    sound = "[default sound]"

    def declare_name(self):
        print("I am a {}".format(self.name))

    def make_sound(self):
        print("My sound is {}".format(self.sound))

    def format_tester(self):
        print("{0}! I am a {1} and because I am a {1} I like to go {0}! {0}!"
              .format(self.sound, self.name))


class Fish(Animal):
    name = "fish"
    sound = "blub blub"


def object_stuff():
    x = Animal()
    x.declare_name()
    x.make_sound()
    x.name = "duck"
    x.sound = "quack"
    x.declare_name()
    x.make_sound()
    x.format_tester()

    y = Fish()
    y.declare_name()
    y.make_sound()
    y.format_tester()
    y.num_legs = 100
    print("%s has %d legs" % (y.name, y.num_legs))
    print("{} has {} legs".format(y.name, y.num_legs))


def walrus():
    if (x := input())[0] == "y":
        print("sup, " + x)


# walrus()
