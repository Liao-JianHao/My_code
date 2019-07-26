# Singleton
# 在内存中只有一个对象，节省内存空间。
# 避免频繁的创建销毁对象，可以提高性能。
# 可以全局访问。
# 全局只有一个接入点，可以更好地进行数据同步控制，避免多重占用

"""单例装饰器"""
from functools import wraps


def singleton(cls):
    instances = {}

    @wraps(cls)
    def wrapper(*args, **kwargs):
        if cls not in instances:  # 判断对象是否在字典中
            instances[cls] = cls(*args, **kwargs)  # 没有就添加至字典中
        return instances[cls]  # 如果有就直接返回

    return wrapper


@singleton
def func():
    pass


obj1 = func()
obj2 = func()

print(id(obj1), id(obj2))


"""重构单例"""
class Singleton:

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):  # hasattr：判断对象是否有'_instance'属性
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

obj3 = Singleton()
obj4 = Singleton()

print(id(obj3), id(obj4))


"""type 创建单例"""

class Singleton(type):

    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]


class func1(metaclass=Singleton):
    pass

obj5 = func1()
obj6 = func1()
print(id(obj5), id(obj6))

