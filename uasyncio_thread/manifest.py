# This list of frozen files doesn't include task.py because that's provided by the C module.
freeze(
    "..",
    (
        "uasyncio_thread/__init__.py",
        "uasyncio_thread/core.py",
        "uasyncio_thread/event.py",
        "uasyncio_thread/funcs.py",
        "uasyncio_thread/lock.py",
        "uasyncio_thread/stream.py",
    ),
    opt=3,
)
