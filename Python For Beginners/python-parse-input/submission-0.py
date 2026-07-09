from typing import List

def read_integers() -> List[int]:
    user_input = input().split(",")
    my_list = []
    for s in user_input:
        my_list.append(int(s))
    return my_list

# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())
