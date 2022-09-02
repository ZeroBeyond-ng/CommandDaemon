#
# Author: ZeroBeyond
# A simple daemon that automatically starts up,
# listen for requests, and executes the command.
#
import os
import signal
import daemon
import lockfile
from flask import Flask  

def program_cleanup():
    pass

def reload_program_config():
    pass

context = daemon.DaemonContext(
    working_directory='/var/cmd_daemon',
    umask=0o002,
    pidfile=lockfile.FileLock('/var/run/cmd_daemon.pid'),
    )

context.signal_map = {
    signal.SIGTERM: program_cleanup,
    signal.SIGHUP: 'terminate',
    signal.SIGUSR1: reload_program_config,
    }

cmd_file = open('cmd.sh', 'w')
context.files_preserve = [cmd_file]

# start the main program
app=Flask(__name__) 
@app.route('/') 
def func():  
    return 'Daemonize Test!'

with context:
    app.run()
