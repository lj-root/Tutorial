"""常用排序算法实现。"""

from __future__ import annotations

from collections.abc import Iterable
from typing import TypeVar

T = TypeVar("T")


def merge_sort(items: Iterable[T]) -> list[T]:
    """使用归并排序返回一个升序排列的新列表。

    归并排序采用“分治”思想：先递归地把序列拆成更小的两半，
    再把已经有序的左右两半合并起来。它不会修改传入的可迭代对象。

    时间复杂度：O(n log n)
    空间复杂度：O(n)
    稳定性：稳定
    """

    values = list(items)
    if len(values) <= 1:
        return values

    middle = len(values) // 2
    left = merge_sort(values[:middle])
    right = merge_sort(values[middle:])

    return _merge(left, right)


def _merge(left: list[T], right: list[T]) -> list[T]:
    """合并两个已排序列表。"""

    merged: list[T] = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    merged.extend(left[left_index:])
    merged.extend(right[right_index:])
    return merged


if __name__ == "__main__":
    numbers = [64, 34, 25, 12, 22, 11, 90]
    print("排序前:", numbers)
    print("排序后:", merge_sort(numbers))
