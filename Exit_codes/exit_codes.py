import sys
import os
import subprocess
import codecs
import collections
import json

'''
all exit codes:
https://www.symantec.com/connect/articles/windows-system-error-codes-exit-codes-description
'''

def script_path():
    '''change current path to script one'''
    current_path = os.path.realpath(os.path.dirname(sys.argv[0]))
    os.chdir(current_path)
    return current_path
    
    
def decode_polish(content):
    ''' to know, how it works '''
    polish_chars = {b'\x88' : bytes('ł', 'utf-8'),
                    b'\xbd' : bytes('Ż', 'utf-8'),
                    b'\xbe' : bytes('ż', 'utf-8'),
                    b'\xab' : bytes('ź', 'utf-8'),
                    b'\x86' : bytes('ć', 'utf-8'),
                    b'\xe4' : bytes('ń', 'utf-8'),
                    b'\x97' : bytes('Ś', 'utf-8'),
                    b'\x98' : bytes('ś', 'utf-8'),
                    b'\xa2' : bytes('ó', 'utf-8'),
                    b'\xa5' : bytes('ą', 'utf-8'),
                    b'\xa9' : bytes('ę', 'utf-8')
                    }
    for key, value in polish_chars.items():
        content = content.replace(key, value)
    # content = content.decode('utf-8')
    return content
    
    
def get_status(value):
    out = subprocess.Popen(['net', 'helpmsg', str(value)], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    response, err = out.communicate()
    # status = decode_polish(response)            # my working(but not the best) function
    status, val = codecs.oem_decode(response)   # vs with using codecs
    status = status.strip()
    return status
    
    
if __name__ == "__main__":
    script_path()
    exit_codes = {}
    for code in range(14080):
        status = get_status(code)
        if status:
            key = str(code).zfill(5)
            print("{}. {}".format(key.rjust(5), status))
            exit_codes[key] = status
            
    # save to json
    exit_codes = collections.OrderedDict(exit_codes)
    with open('exit_codes.json', 'w') as fp:
        json.dump(exit_codes, fp, sort_keys=True, indent=4, ensure_ascii=False)
        
        
    '''
    # to get the correct codec
    for item in dir(codecs)[35:]:
        try:
            out = getattr(codecs, item)(chr(322))
            print(item, out)
            # looking for b'\x88'
        except:
            # print("failed with: {}".format(item))
            pass
    '''
    
    '''
    # string as method
    some = "this"
    var = "upper"
    out = getattr(some, var)()
    print(out)
    '''
    