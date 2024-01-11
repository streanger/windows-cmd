import csv
import ctypes
import json
import os
import subprocess
import sys
import time
from pathlib import Path

from rich import print


def now():
    return time.strftime('%Y%m%d%H%M%S')


def write_json(filename, data):
    """write to json file"""
    with open(filename, 'w', encoding='utf-8') as fp:
        json.dump(data, fp, sort_keys=True, indent=4, ensure_ascii=False)
    return True


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
    os.chdir(str(Path(__file__).parent))
    rerun_as_admin()

    # **** run command ****
    # command = "Get-AppxPackage -AllUsers | Select Name, PackageFullName"
    # command = "Get-AppxPackage -AllUsers | Select Name, PackageFullName | Export-Csv -Path .\output.csv -NoTypeInformation"
    command = "Get-AppxPackage -AllUsers | Select Name, PackageFullName | ConvertTo-Csv -NoTypeInformation"
    response = run(command)
    stdout = response.stdout.decode('852')
    stderr = response.stderr.decode('852')
    if not stdout:
        print(stderr)
        sys.exit(1)

    # **** parse output ****
    csv_reader = csv.DictReader(stdout.splitlines())
    packages = {row['Name']: row['PackageFullName'] for row in csv_reader}
    print(packages)

    # **** save to json file ****
    directory = Path('appxpackages')
    directory.mkdir(exist_ok=True)
    out = f'appxpackages-{now()}.csv'
    path = directory.joinpath(out)
    write_json(path, packages)
    print(f'[*] data saved to: {path}')
