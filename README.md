Uasyncio implementation running independently on the 2nd core of the Raspberry Pi Pico.

Changes are minimal, it's just a separate module with an added feature for creating tasks thread_safe.
Tasks can be created from the main thread but tasks running on the 2nd core can't create Tasks on the main core uasyncio.
Don't await Tasks created for a loop in a different thread!

Currently this module can only be used on one other thread/core as it relies on variables that are bound to the module itself.
It can be used on multiple threads/cores if it gets renamed and imported as a completely separate module, e.g. uasyncio_thread2.
This increases RAM usage a lot but is currently the simplest way of supporting a uasyncio loop in a different thread/core.
A thread support inside a single uasyncio module would require a major rewrite of the module making it bigger and slower without any benefit for all single-core ports/devices.