class Event(list):
    """
    Represents an event to which functions can subscribe. It extends the functionality of a list to manage
    a collection of functions that will be called when the event is triggered.
    """

    def __call__(self, *args, **kwargs):
        """
        Invokes the subscribed functions with the given arguments.
        self is list of function.
        """
        for item in self:
            item(*args, **kwargs)


class Person:

    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.falls_ill = Event()

    def catch_a_cold(self):
        """
        Triggers the event of the person falling ill, invoking all subscribed functions.
        """
        self.falls_ill(self.name, self.address)


def call_doctor(name, address):
    print(f'A doctor has been called to {address}')


if __name__ == '__main__':
    person = Person('Sherlock', '221B Baker St')

    # person.falls_ill.append(lambda name, addr: print(f'{name} is ill'))

    person.falls_ill.append(call_doctor)

    person.catch_a_cold()

    # Removing subscriptions is also supported
    person.falls_ill.remove(call_doctor)
    person.catch_a_cold()
