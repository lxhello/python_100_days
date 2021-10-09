class Person(object):
    # Python是一门动态语言。通常，动态语言允许我们在程序运行时给对象绑定新的属性或方法
    # 限定Person对象只能绑定_name, _age和_gender属性
    __slots__ = ("_name", "_age", "_gender")

    def __init__(self, name, age):
        self._name = name
        self._age = age

    # 访问器 - getter方法
    @property
    def name(self):
        return self._name

    # 通过一个getter可以让外界访问到函数内的值
    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        self._age = age

    def play(self):
        print("%s is play joyful games")

    def watch_tv(self):
        if self._age > 18:
            print("%s in watch kung_fu" % self._name)
        else:
            print("%s in watch cartoon" % self._name)


class Student(Person):

    def __init__(self, name, age, grade):
        super().__init__(name, age)  # 继承父类Person
        self._grade = grade

    @property
    def grade(self):
        return self._grade

    @grade.setter
    def grade(self, grade):
        self._grade = grade

    def study(self, course):
        print("%s %s is studying %s " % (self._grade, self._name, course))


class Teacher(Person):

    def __init__(self, name, age, title):
        super().__init__(name, age)
        self._title = title

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        self._title = title

    def teach(self, course):
        print("%s%s is teaching %s" % (self._name, self._title, course))


def main():
    stu = Student("zhang_san", 15, "high_school")
    stu.study("math")
    teac = Teacher("wang_si", 32, "profess")
    teac.teach('math')
    teac.watch_tv()


if __name__ == "__main__":
    main()
