import sys
import subprocess
import os

def launch_ida():
    connection_file = sys.argv[1]
    ida_location = sys.argv[2]
    env = dict(
            JUPYTER_CONNECTION=connection_file,
            **os.environ
        )
    env["WSLENV"] = "JUPYTER_CONNECTION/p"
    ida_process = subprocess.Popen(
        [ida_location],
        env=env
    )
    ida_process.wait()


if __name__ == '__main__':
    launch_ida()
