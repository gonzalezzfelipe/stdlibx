def snake_case(string):
    """Turn string to snake_case.

    'Example string' ==> 'example_string'."""
    return string.lower().replace(' ', '_')


def snake2normal(string):
    """Turn string to snake_case.

    'example_string' ==> 'Example string'."""
    return string.replace('_', ' ').capitalize()


def close_match_exception(evaluate, available_list, var_name):
    """Raise error if variable defined is not in available arguments.

    Parameters
    ----------
    evaluate : str
        String to evaluate.
    available_list : list of str
        List of accepted arguments.
    var_name : str
        Name of variable being evaluated.

    Returns
    -------
    str
        Returns evaluating value.

    Raises
    -------
    ValueError
        Raises value error if evaluate is not on available_list.

    """
    if evaluate not in available_list:
        try:
            close = get_close_matches(evaluate, available_list, n=1)[0]
            error = "'{}' is not an available {}. Did you mean '{}'?"
            error = error.format(evaluate, var_name, close)
        except IndexError:
            error = "'{}' is not an available {}.".format(
                evaluate, var_name)
            raise ValueError(error)
    return eval


def tabulate(table, extra_space=2, sep='|', blank=' '):
    # Row template
    sizes = [max(map(len, map(str, col))) + extra_space for col in zip(*table)]
    template = ''.join(f'{sep}%s' for _ in sizes) + sep

    def center_string(s, size, blank):
        s = str(s)
        missing = size - len(s)
        right = missing // 2
        left = missing - right
        return left * blank + s + right * blank

    # Pretty print
    return '\n'.join(
        template % tuple(
            center_string(s, size, blank) for s, size in zip(row, sizes))
        for row in table)


if __name__ == '__main__':
    table = [
        ['col0', 'col1', 'col2'],
        [12390, 'laknvas', 120111]]
    print(tabulate(table, extra_space=4, sep='/', blank='*'))
