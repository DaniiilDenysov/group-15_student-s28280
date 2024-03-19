def create_range_list(a, b):
    range_list = [x * x for x in range(a, b)]
    return range_list


lower_bound = int(input("Please enter lower bound:"))
upper_bound = int(input("Please enter upper bound:"))
print(create_range_list(lower_bound, upper_bound))
