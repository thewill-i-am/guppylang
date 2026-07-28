from guppylang import guppy
from guppylang.std.lang import Drop, owned
from guppylang.std.quantum import qubit


@guppy.protocol
class DropProto(Drop):
    """Empty droppable protocol"""


@guppy.struct
class LinearType:
    q: qubit


@guppy
def foo[T: DropProto](x: T @ owned) -> None:
    pass


@guppy
def main(q: qubit) -> None:
    foo(LinearType(q))


main.compile()
