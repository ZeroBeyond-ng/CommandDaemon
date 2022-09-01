#
# Author: ZeroBeyond
# A simple daemon that automatically starts up,
# listen for requests, and executes the command.
#
import os
import grp
import signal
import daemon
import lockfile

def initial_program_setup():
    pass

def do_main_program():
    pass

def program_cleanup():
    pass

def reload_program_config():
    pass

context = daemon.DaemonContext(
    working_directory='/var/lib/foo',
    umask=0o002,
    pidfile=lockfile.FileLock('/var/run/spam.pid'),
    )

context.signal_map = {
    signal.SIGTERM: program_cleanup,
    signal.SIGHUP: 'terminate',
    signal.SIGUSR1: reload_program_config,
    }

mail_gid = grp.getgrnam('mail').gr_gid
context.gid = mail_gid

important_file = open('spam.data', 'w')
interesting_file = open('eggs.data', 'w')
context.files_preserve = [important_file, interesting_file]

initial_program_setup()

with context:
    do_main_program()
