import random


def _integer_list(lists_num, list_size, min_val, max_val, scatter_radius):
    min_center = min_val + scatter_radius
    max_center = max_val - scatter_radius

    transposed_lists = []

    for i in range(list_size):

        # Center should be evaluated for each transposed list
        # so they won't have the same center.
        center = random.uniform(min_center, max_center)

        list_min = round(center - scatter_radius)
        list_max = round(center + scatter_radius)

        transposed_list = []

        for j in range(lists_num):
            transposed_list.append(random.randint(list_min, list_max))
            
        transposed_lists.append(transposed_list)

    # And now the very interesting:
    # Transpose lists back to get a list of lists where
    # for each two lists, i-th element of one list
    # is correlated with i-th element of another.
    # It's done by unpacking transposed_lists,
    # zipping them and converting each tuple returned by zip to a list (done with map())
    integer_list = list(map(list, zip(*transposed_lists)))
    return integer_list


def generate_correlated_lists(lists_num, list_size, min_val, max_val, scatter, integer=True):

    if max_val < min_val:
        raise ValueError('Max number must be greater than min')

    diameter = max_val - min_val

    scatter = abs(scatter)  # force the scatter to be positive
    if scatter > diameter:
        raise ValueError('Scatter must not be greater than the difference between max and min value')

    scatter_radius = scatter / 2  # python 3, must be floating point!

    if integer == True:
        return _integer_list(lists_num, list_size, min_val, max_val, scatter_radius)
