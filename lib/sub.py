import subprocess
import time
import os

class Sub():
    
    def __init__(self, PROXIES):
        self._PROXIES = PROXIES
        
    def starting_a_thread(self, FILENAME):
        commond = f"/usr/bin/python3 stream.py {self._PROXIES} {FILENAME}"
        try:
            pid = subprocess.Popen(
                args=commond,
                shell=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                preexec_fn=os.setsid
            )
        except Exception as error:
            return False
        return pid.pid
             
    
    