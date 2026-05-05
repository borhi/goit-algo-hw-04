import random
from timeit import Timer


def insertion_sort(arr: list[int]) -> None:
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


def merge_sort(arr: list[int]) -> list[int]:
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    return merge(merge_sort(left_half), merge_sort(right_half))


def merge(left: list[int], right: list[int]) -> list[int]:
    merged: list[int] = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    while left_index < len(left):
        merged.append(left[left_index])
        left_index += 1

    while right_index < len(right):
        merged.append(right[right_index])
        right_index += 1

    return merged


def measure(stmt) -> float:
    timer = Timer(stmt)
    n_runs, total = timer.autorange()
    return total / n_runs


def random_list(n: int) -> list[int]:
    rnd = random.Random(42 + n)
    xs = list(range(n))
    rnd.shuffle(xs)
    return xs


def main() -> None:
    sizes = [8000, 30000, 80000]
    insert_limit = 8000

    print("n\tInsert\tMerge\tTimsort")

    for n in sizes:
        data = random_list(n)
        t_merge = measure(lambda: merge_sort(list(data)))
        t_tm = measure(lambda: sorted(data))

        if n <= insert_limit:
            t_ins = measure(lambda: insertion_sort(data.copy()))
            print(
                f"{n}\t{t_ins * 1000:.2f}\t{t_merge * 1000:.2f}\t"
                f"{t_tm * 1000:.2f}"
            )
        else:
            print(
                f"{n}\t-\t{t_merge * 1000:.2f}\t{t_tm * 1000:.2f}"
            )


if __name__ == "__main__":
    main()
