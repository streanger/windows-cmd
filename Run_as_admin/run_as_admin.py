import sys
import os
import ctypes

def script_path():
    current_path = os.path.realpath(os.path.dirname(sys.argv[0]))
    os.chdir(current_path)
    return current_path
    
    
def run_as_admin(commands, cmdLine=None, wait=True):
    ''' based on --> https://stackoverflow.com/questions/19672352/how-to-run-python-script-with-elevated-privilege-on-windows'''
    import win32api, win32con, win32event, win32process
    from win32com.shell.shell import ShellExecuteEx
    from win32com.shell import shellcon
    
    python_exe = sys.executable
    
    if cmdLine is None:
        cmdLine = [python_exe] + commands
        
    cmd = cmdLine[0]
    params = ' '.join(commands)
    showCmd = win32con.SW_SHOWNORMAL
    lpVerb = 'runas'
    procInfo = ShellExecuteEx(nShow=showCmd,
                              fMask=shellcon.SEE_MASK_NOCLOSEPROCESS,
                              lpVerb=lpVerb,
                              lpFile=cmd,
                              lpParameters=params)     
    if wait:
        procHandle = procInfo['hProcess']    
        obj = win32event.WaitForSingleObject(procHandle, win32event.INFINITE)
        rc = win32process.GetExitCodeProcess(procHandle)
        #print "Process handle %s returned code %s" % (procHandle, rc)
    else:
        rc = None
    return rc
    
    
if __name__ == "__main__":
    script_path()
    commands = ['-i', 'test.py']
    run_as_admin(commands)
