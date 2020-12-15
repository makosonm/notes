log = getLogger()
# Use an absolute path to prevent file rotation trouble.
logfile = os.path.abspath("mylogfile.log")
# Rotate log after reaching 512K, keep 5 old copies.
rotateHandler = ConcurrentRotatingFileHandler(logfile, "a", 512 * 1024, 5)
log.addHandler(rotateHandler)
log.setLevel(INFO)

if __name__ == "__main__":
    import os
    import time
    from logging import INFO, getLogger

    from cloghandler import ConcurrentRotatingFileHandler

    log = getLogger()
    # Use an absolute path to prevent file rotation trouble.
    logfile = os.path.abspath("mylogfile.log")
    # Rotate log after reaching 512K, keep 5 old copies.
    rotateHandler = ConcurrentRotatingFileHandler(logfile, "a", 512 * 1024, 5)
    log.addHandler(rotateHandler)
    log.setLevel(INFO)

    while True:
        log.info(str(os.getpid()) + " " + str(time.time()))
        time.sleep(1)
