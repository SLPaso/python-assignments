python
class Dog:
    def make_sound(self):
        return "Woof!"

class Cat:
    def make_sound(self):
        return "Meow!"

def process_sound(sound_object):
    print(sound_object.make_sound())

# Example usage
process_sound(Dog())
process_sound(Cat())
