#!/usr/bin/python3
import fcntl,time


with open("lock") as f:
    print("locking")
    fcntl.flock(f,fcntl.LOCK_EX)
    print("locked")
    print("sleeping 10 seconds")
    time.sleep(10)
