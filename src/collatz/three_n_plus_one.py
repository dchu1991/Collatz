# %%
from typing import Optional


class ThreeNPlusOne:
    """associate 1 int with 1 instance and the intermediate steps leading
    to a loop.  all nums in the steps are considered as visited such that
    we don't have to call the recursion again."""

    _visited: dict[int, "ThreeNPlusOne"] = {}

    def __new__(cls: type["ThreeNPlusOne"], num: int) -> "ThreeNPlusOne":
        """no more than 2 instances for a given num"""
        if (obj := cls._visited.get(num)) is not None:
            return obj
        obj = super().__new__(cls)
        cls._visited[num] = obj
        return obj

    def __init__(self, num: int, intermediate_steps: Optional[tuple[int, ...]] = None) -> None:
        self.num = num

        # no reset everytime when called.
        if not hasattr(self, "intermediate_steps"):
            self.intermediate_steps = (
                intermediate_steps if intermediate_steps is not None else (
                    self.num,)
            )

        next_num = ThreeNPlusOne.next_num(num)
        # print(f"{self}, \t{next_num = }")

        # main recursion logic
        if next_num not in self.intermediate_steps:
            if next_num not in self._visited:
                next_ins = ThreeNPlusOne(next_num)
                self.intermediate_steps += next_ins.intermediate_steps
            else:
                next_ins = self._visited[next_num]
                if self.num != next_ins.intermediate_steps[-1]:
                    self.intermediate_steps += next_ins.intermediate_steps

    def __str__(self) -> str:
        return f"initialized/called with {self.num = }"

    @staticmethod
    def next_num(num: int) -> int:
        if num & 1:
            return 3 * num + 1
        else:
            return num >> 1

# %%


def recursive_iter(
    n: int, steps: int = 0, res_str: str = "", intermediate_steps: Optional[tuple[int, ...]] = None
) -> tuple[tuple[int, ...], int]:

    intermediate_steps = (
        intermediate_steps if intermediate_steps is not None else tuple()
    )

    if n in intermediate_steps:
        res_str += f"reached terminate condition after {steps = }"
        print(res_str)
        return intermediate_steps, steps
    else:
        res_str += f"{n} -> "
        if n & 1:
            return recursive_iter(
                (3 * n + 1), steps + 1,
                res_str, intermediate_steps + (n,)
            )
        else:
            return recursive_iter(n >> 1, steps + 1,
                                  res_str, intermediate_steps + (n,))
