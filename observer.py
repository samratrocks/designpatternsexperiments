# Quick and dirty iteration of the Observer pattern (GOF)
class Subject:
    def __init__(self):
        self.list_of_observers = [
        ]
        
    def attach(self, observer):
        print('attaching %s' % (observer))
        if (not(observer in self.list_of_observers)):
            self.list_of_observers.append(observer)

    def detach(self, observer):
        print('detaching %s' % (observer))
        if (observer in self.list_of_observers):
            self.list_of_observers.remove(observer)

    def notify(self):
        for observer in self.list_of_observers:
            observer.update()


class Observer():
    def __init__(self):
        self.counter = 0
        
    def update(self):
        self.counter += 1
        print('Counter: %d' % self.counter)
        

s = Subject()
o1 = Observer()
o2 = Observer()

s.attach(o1)
s.attach(o2)
s.notify()
