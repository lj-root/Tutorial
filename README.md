# Tutorial

这个仓库包含一个 Python 排序算法示例。

## 归并排序

`algorithms/sorting.py` 提供了 `merge_sort` 函数，它会返回一个新的升序列表，并且不会修改原始输入。

```python
from algorithms.sorting import merge_sort

numbers = [64, 34, 25, 12, 22, 11, 90]
print(merge_sort(numbers))  # [11, 12, 22, 25, 34, 64, 90]
```

运行示例：

```bash
python algorithms/sorting.py
```

运行测试：

```bash
python -m unittest discover -s tests
```
