
class _NoValueMeta(type):
    def __repr__(cls) -> str:
        return "NoValue"

    def __str__(cls) -> str:
        return "NoValue"

    def __call__(cls, *args, **kwargs):
        raise TypeError("NoValue cannot be instantiated")

    def __bool__(cls) -> bool:
        raise TypeError("NoValue cannot be cast to bool")


class NoValue(metaclass=_NoValueMeta):
    def __new__(cls, *args, **kwargs):
        raise TypeError("NoValue cannot be instantiated")
