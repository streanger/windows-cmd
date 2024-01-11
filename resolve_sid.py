import pywintypes
import win32security


def sid_to_user(sid):
    """convert Windows SID to corresponding username
    alternatively use command:
    whoami /user
    """
    sid = win32security.ConvertStringSidToSid(sid)
    try:
        name, domain, _ = win32security.LookupAccountSid(None, sid)
    except pywintypes.error as err:
        print(err)
        return ''
    user = f'{domain}\\{name}'
    return user


def user_to_sid(system_name, account_name):
    sid, domain, type = win32security.LookupAccountName(system_name, account_name)
    sid_string = win32security.ConvertSidToStringSid(sid)
    return sid_string


sid = 'S-1-5-21-123456789-1234567890-1234567890-1234'
resolved_user = sid_to_user(sid)
print(f'{sid} -> {resolved_user}')

user = 'Administrator'
resolved_sid = user_to_sid(None, user)
print(f'{user} -> {resolved_sid}')
