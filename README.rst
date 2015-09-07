thread_timeout
==============

Library to safely execute code without fear of the TASK_UNINTERRUPTIBLE state
-----------------------------------------------------------------------------

`thread_timeout` allows to run a piece of python code safely regardless 
of TASK_UNINTERRUPTIBLE issues.

It provides single decorator, adding a timeout for the function call.


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


`thread_timeout` works by running specified function in separate thread and waiting
for timeout (or finalization) of the thread to return value or raise Exception.
If thread is not finished before timeout, `thread_timeout` may try to terminate
thread according to kill_wait value (see below).

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
`ExecTimeoutException` - function did not finish on time, timeout (base class for all following exceptions)
`KilledExecTimeoutException` - there was a timeout and thread with function was killed successfully
`FailedKillExecTimeoutException` - there was a timeout and kill attempt but the thread refuses to die
`NotKillExecTimeoutException` - there was a timeout and there was no attempt to kill thread
