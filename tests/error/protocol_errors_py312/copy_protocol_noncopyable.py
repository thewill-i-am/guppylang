from guppylang import guppy
from guppylang.std.lang import Copy
from guppylang.std.quantum import qubit


@guppy.protocol
class CopyProto(Copy):
    """Empty copyable protocol"""


@guppy.struct
class LinearType:
    q: qubit


@guppy
def foo[T: CopyProto](x: T) -> tuple[T, T]:
    return x, x


@guppy
def main(q: qubit) -> None:
    foo(LinearType(q))


main.compile()
