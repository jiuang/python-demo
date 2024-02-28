class EmptyClass:
    pass  # 起到占位符作用，即当前类下午任何属性和方法


class CommonClass:
    __id = 1  # 类中私有属性，以两个下划线开头，无法通过CommonClass.__id调用到
    name = '钱多多'
    __slots__ = ('age', 'idcard')  # 只允许动态扩展age属性

    def __init__(self):  # 构造方法，在外界执行 s1 = CommonClass() 时，会先触发此方法
        print('我是类中构造方法')

    def __del__(self):  # 析构方法，在对象销毁时先触发此方法
        print('我是类中析构方法')

    # todo 咋也可以被类直接调用呢？？？？？
    def commonClassMethod(self):
        print('我不能被类直接调用')

    # 用@classmethod修饰的方法，可以通过类.方法名的方式直接调用，有self参数，否则只能通过类的实例去调用
    @classmethod
    def testClassMethod(cls, p1, p2):
        print('我是类方法，可以被类直接调用，有self参数')
        print(p1+p2)

    # 用@staticmethod，可以通过类.方法名的方式直接调用，没有self参数，否则只能通过类的实例去调用
    @staticmethod
    def testStaticMethod(p1, p2):
        print('我静态方法，可以被类直接调用，且没有self参数')
        print(p1+p2)


# 内置函数isinstance、issubclass、type
class Person:  # 定义Person类
    pass


class Student(Person):  # 以Person类作为父类定义子类Student
    pass


class Flower:  # 定义Flower类
    pass


def testIsinstance():
    stu = Student()  # 创建Student类对象stu
    f = Flower()  # 创建Flower对象f
    print('stu是Person类或其子类对象：', isinstance(stu, Person))
    print('stu是Student类或其子类对象：', isinstance(stu, Student))
    print('f是Person类或其子类对象：', isinstance(f, Person))


def testIssubclass():
    print('Student是Person类的子类：', issubclass(Student, Person))
    print('Flower是Person类的子类：', issubclass(Flower, Person))


def testType():
    stu = Student()  # 创建Student类对象stu
    f = Flower()  # 创建Flower对象f
    print('stu对象所属的类：', type(stu))
    print('f对象所属的类：', type(f))
    print('stu是Person类对象：', type(stu) == Person)
    print('stu是Student类对象：', type(stu) == Student)
