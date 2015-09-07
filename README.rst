thread_timeout
==============

`thread_timeout` is a Python (2) library. It provides a simple decorator `@thread_timeout` for executing of a potentially long-running operation and auto-terminating if operation hasn't finished in a fixed amount of time.

This allows a python program avoiding TASK_UNINTERRUPTIBLE state.


Example of the usage:

.. code-block:: python

    import thread_timeout

    @thread_timeout(10, kill=False)
    def NFS_read(path):
        file(path, 'r').read()

    try:
        print("Result: %s" % NFS_read('broken_nfs/file'))
    except ExecTimeoutException:
        print ("NFS seems to be hung")


`thread_timeout` works by running specified function in separate thread while waiting
for timeout (or finalization) of the thread. Decorated function returns value if the function completed before `timeout` seconds, otherwise it may try to terminate thread and then throws an exception according to kill value (see below) .
Before trying to terminate thread decorator will wait `kill_wait` seconds. 

.. code-block:: python

    thread_timeout(timeout, kill=True, kill_wait=0.1)

- `timeout` - seconds, floating, how long to wait thread.
- `kill` - if True (default) attempt to terminate thread with function.
- `kill_wait` - how long to wait after killing before reporting an unresponsive thread.

THREAD KILLING
--------------
Thread killing implemented on python level: it will terminate python code, but will not terminate any IO operations or subprocess calls. 

Exceptions:
-----------
- `ExecTimeoutException` - function did not finish on time, timeout (base class for all following exceptions)
- `KilledExecTimeoutException` - there was a timeout and thread with function was killed successfully
- `FailedKillExecTimeoutException` - there was a timeout and kill attempt but the thread refuses to die
- `NotKillExecTimeoutException` - there was a timeout and there was no attempt to kill thread

