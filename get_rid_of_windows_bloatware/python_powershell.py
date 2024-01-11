import ctypes
import os
import sys
import subprocess


def rerun_as_admin():
    """rerun script as admin if not already running as admin"""
    if ctypes.windll.shell32.IsUserAnAdmin():
        return True
    INTERACTIVE_MODE = "-i "
    args = INTERACTIVE_MODE + " ".join(sys.argv)
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, args, None, 1)
    os.abort()  # simplest way to close console even if interactive mode is enabled


def run(cmd):
    response = subprocess.run(["powershell", "-Command", cmd], capture_output=True)
    return response


if __name__ == '__main__':
    rerun_as_admin()
    command = "Get-AppxPackage -AllUsers | Select Name, PackageFullName"
    response = run(command)
    stdout = response.stdout.decode('852')
    stderr = response.stderr.decode('852')
    output = stdout or stderr
    print(output)
    