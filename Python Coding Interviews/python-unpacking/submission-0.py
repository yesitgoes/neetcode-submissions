from typing import List, Tuple


def sum_3_integers(triplet: List[int]) -> int:
    a, b, c = triplet
    triple_sum = a + b + c
    return triple_sum


def compute_volume(box_dimensions: Tuple[int, int, int]) -> int:
    w, h, d = box_dimensions
    v = w * h * d
    return v
  

# do not modify below this line
print(sum_3_integers([1, 2, 3]))
print(sum_3_integers([4, 6, 2]))

print(compute_volume((1, 2, 3)))
print(compute_volume((3, 2, 1)))
print(compute_volume((3, 9, 7)))
