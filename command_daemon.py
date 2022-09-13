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
if not os.path.exists(work_dir):
    os.mkdir(work_dir)

stderr_file = open('/var/tmp/cmd_daemon/stderr.txt', 'w+')
stdout_file = open('/var/tmp/cmd_daemon/stdout.txt', 'w+')
log_file = open('/var/tmp/cmd_daemon/daemon-log.txt', 'w+')

def program_cleanup():
    pass

def reload_program_config():
    pass


context = daemon.DaemonContext(
    working_directory=work_dir,
    umask=0o002,
    pidfile=lockfile.FileLock('/var/tmp/cmd_daemon/lock.pid'),
    stderr=stderr_file,
    stdout=stdout_file
    )

context.signal_map = {
    signal.SIGTERM: program_cleanup,
    signal.SIGHUP: 'terminate',
    signal.SIGUSR1: reload_program_config,
    }

cmd_file = open('cmd.sh', 'w')

context.files_preserve = [cmd_file, log_file]

def exec():
    subprocess.call("cmd.sh")

def create_app():
    # start the main program
    app=Flask(__name__) 
    @app.route('/', methods=["POST", "GET"]) 
    def func():  
        log_file.write("aaaaaaaa\n")
        if request.method == 'POST':
            cmd = request.form['command']
            if cmd == 'exec':
                exec()
        else:
            return "Hello CmdDaemon!"

    return app


def create_app1():
    # start the main program
    app=Flask(__name__) 
    @app.route('/') 
    def func():  
        return "Hello CmdDaemon!"

    return app

def logging_forever(log_file):
    while True:
        print("Daemon")
        log_file.write("Logging...")

def run_web_app():
    app = create_app1()
    app.run(host = '0.0.0.0', port=17777)

with context:
    run_web_app()
    logging_forever(log_file)
