#
# Author: ZeroBeyond
# A simple daemon that automatically starts up,
# listen for requests, and executes the command.
#
import os
import signal
import daemon
import lockfile
import subprocess
from flask import Flask  

# constants 
work_dir='/var/tmp/cmd_daemon' 


def program_init():
    if not os.path.exists(work_dir):
        os.mkdir(work_dir)


def program_cleanup():
    pass

def reload_program_config():
    pass

context = daemon.DaemonContext(
    working_directory=work_dir,
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

def exec():
    subprocess.call("cmd.sh")

# start the main program
app=Flask(__name__) 
@app.route('/', methods=["POST"]) 
def func():  
    if request.method == 'POST':
        cmd = request.form['command']
        if cmd == 'exec':
            exec()
    else:
        return "Hello CmdDaemon!"

program_init()

with context:
    app.run(host = '0.0.0.0', port=17777)
