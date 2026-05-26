class Foo:
    def __init__(self):
        self.step = 1

    def first(self, printFirst: 'Callable[[], None]') -> None:
        if self.step == 1:
            # printFirst() outputs "first". Do not change or remove this line.
            printFirst()
            self.step += 1

    def second(self, printSecond: 'Callable[[], None]') -> None:
        while True:
            if self.step == 2:
                # printSecond() outputs "second". Do not change or remove this line.
                printSecond()
                self.step += 1
                break

    def third(self, printThird: 'Callable[[], None]') -> None:
        while True:
            if self.step == 3:
                # printThird() outputs "third". Do not change or remove this line.
                printThird()
                self.step = 0
                break