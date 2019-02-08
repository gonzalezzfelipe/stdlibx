import datetime as dt
import re

DATE_FORMATS = [
    '%Y-%m-%d %H:%M:%S',
    '%Y-%m-%d',
    '%Y%m%d']


def dateparse(string, fmt=None):
    if fmt is not None:
        return dt.datetime.strptime(string, fmt)
    else:
        for fmt in DATE_FORMATS:
            try:
                return dt.datetime.strptime(string, fmt)
            except (ValueError, re.error):
                pass
        raise ValueError('time data "{}" does not match formats {}'.format(
            string, tuple(formats)))


def isfirstofmonth(date):
    """Evaluate wether date is the first day of the month."""
    return date.month != (date - dt.timedelta(days=1)).month


def islastofmonth(date):
    """Evaluate wether date is the first day of the month."""
    return date.month != (date + dt.timedelta(days=1)).month


def daterange(
        initial,
        final=None,
        amount=None,
        step=dt.timedelta(days=1),
        fmt=None):
    """Get range of dates.

    Parameters
    ----------
    initial : str or datetime.datetime
        Initial date of range. If string, will be parsed by the
        `dateparse` function and output will have the same format.
    final : str or datetime.datetime, optional
        Final date of range, not included (mimic stdlib's range). If
        string, will be parsed by the dateparse function. If undefined,
        `amount` must be defined.
    amount : int, optional
        Amount of values to yield. If undefined, `final` must be
        defined.
    step : dt.timedelta, optional
        Time delta between yielded dates.
    fmt : str, optional
        String defining date format of input and output. If defined,
        output will be formated as string.

    Yields
    ------
    datetime.datetime or str
        If `initial` is string or `fmt` is defined, the yielded output
        will be a string. Else, a datetime.datetime object.

    Raises
    -------
    ValueError
        If both `final` and `amount` are undefined.

    """
    if isinstance(initial, str):
        fmt = fmt or getdatefmt(initial)
        initial = dateparse(initial, fmt)
    if final is None and amount is None:
        raise ValueError('Either "final" or "amount" must be defined.')
    if final is None:
        final = initial + (amount + 1) * step
    else:
        if isinstance(final, str):
            final = dateparse(final, fmt)
    while initial < final:
        if fmt:
            yield initial.strftime(fmt)
        else:
            yield initial
        initial += step


def getdatefmt(string, fmts=None):
    """Get format of a date string."""
    fmts = fmts or []
    for fmt in fmts + DATE_FORMATS:
        try:
            dt.datetime.strptime(string, fmt)
            return fmt
        except ValueError:
            pass
    raise ValueError('time data "{}" does not match formats {}'.format(
        string, tuple(fmts)))


if __name__ == '__main__':
    print([date for date in daterange('2019-01-30', amount=10)])
