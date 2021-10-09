from time import sleep, time, localtime
import os


class Clock(object):

    def __init__(self, hour=0, minute=0, second=0):
        self._hour = hour
        self._minute = minute
        self._second = second

    @classmethod
    def now_time(cls):
        c_time = localtime(time())
        return cls(c_time.tm_hour, c_time.tm_min, c_time.tm_sec)

    def run(self):
        self._second += 1
        if self._second == 60:
            self._second = 0
            self._minute += 1
            if self._minute == 60:
                self._minute = 0
                self._hour += 1
                if self._hour == 24:
                    self._hour = 0

    def show_time(self):
        return '%02d:%02d:%02d' % (self._hour, self._minute, self._second)


def main():
    # clock = Clock.now_time() //current time
    clock = Clock(23, 59, 59)  # clock time
    while True:
        print(clock.show_time())
        sleep(1)
        os.system("clear")
        clock.run()


if __name__ == "__main__":
    main()
