from abc import abstractmethod, ABCMeta


# abc 抽象基类

class Employee(metaclass=ABCMeta):
    def __init__(self, no, name):
        self.no = no
        self.name = name

    @abstractmethod
    # 如果不执行就不调用 """结算月薪(抽象方法)"""
    def get_salary(self):
        pass


class Manager(Employee):
    def get_salary(self):
        return 15000


class Programming(Employee):
    def __init__(self, no, name, work_hour=0):
        self.work_hour = work_hour
        super().__init__(no, name)

    def get_salary(self):
        return 200 * self.work_hour


class Saleman(Employee):
    def __init__(self, no, name, sale=0):
        self.sale = sale
        super().__init__(no, name)

    def get_salary(self):
        return 1800 + self.sale * 0.05