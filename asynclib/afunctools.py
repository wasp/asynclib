import asyncio
import functools as _functools


def partial(func, *args, **keywords):
    """Wrapper around the standard library functools partial,
    this adds support for async functions."""
    # In case somehow we don't maintain feature parity and
    # someone uses it on a traditional func
    if not asyncio.iscoroutinefunction(func):
        return _functools.partial(func, *args, **keywords)

    if hasattr(func, 'func'):
        args = func.args + args
        tmpkw = func.keywords.copy()
        tmpkw.update(keywords)
        keywords = tmpkw
        del tmpkw
        func = func.func

    async def newfunc(*fargs, **fkeywords):
        newkeywords = keywords.copy()
        newkeywords.update(fkeywords)
        return await func(*(args + fargs), **newkeywords)

    newfunc.func = func
    newfunc.args = args
    newfunc.keywords = keywords
    return newfunc

