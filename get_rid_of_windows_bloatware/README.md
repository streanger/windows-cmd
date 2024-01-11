# get rid of windows bloatware

some commands & tips of how to get rid of windows bloatware

## configurations stuff

threads about GPO install:
- https://answers.microsoft.com/en-us/windows/forum/all/how-to-enable-gpeditmsc-in-windows-10-home/9f2ab0da-3821-48e6-9205-fd7755b904f4?page=3
- https://www.itechtics.com/enable-gpedit-windows-10-home/
- https://woshub.com/group-policy-editor-gpedit-msc-for-windows-10-home/
- https://www.majorgeeks.com/content/page/enable_group_policy_editor_in_windows_10_home_edition.html
- https://www.microsoft.com/en-us/download/details.aspx?id=25250

commands to install gpedit.msc on Windows 10 Home (from admin cmd):
- `FOR %F IN ("%SystemRoot%\servicing\Packages\Microsoft-Windows-GroupPolicy-ClientTools-Package~*.mum") DO (DISM /Online /NoRestart /Add-Package:"%F")`
- `FOR %F IN ("%SystemRoot%\servicing\Packages\Microsoft-Windows-GroupPolicy-ClientExtensions-Package~*.mum") DO (DISM /Online /NoRestart /Add-Package:"%F")`

## disable annoying features & remove bloatware

disable telemetry:
- https://www.geekbits.io/how-to-disable-telemetry-on-windows-10/
- https://wethegeek.com/how-to-disable-telemetry-and-data-collection-in-windows-10/
- from GPO -> `Computer Configuration` > `Administrative Templates` > `Windows Components` > `Data collection and Preview Builds` > `Allow Telemetry` (set to disabled)
- from services.msc -> `Connected User Experiences and Telemetry`
- from task scheduler -> `Task Scheduler Library` > `Microsoft` > `Windows` > `Customer Experience Improvement Program` > `Consolidator` (disable it)

disable bing search and others:
- https://techlabs.blog/categories/guides/disable-bing-search-windows-10-start-menu-using-gpo
- https://www.youtube.com/watch?v=DiFgesc-dpQ
- `HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Search` -> create `BingSearchEnabled` (and set to 0)

list all packages (from admin powershell):
- `Get-AppxPackage -AllUsers | Select Name, PackageFullName`
- `Get-AppxPackage -AllUsers | Select Name, PackageFullName | Select-String pattern`

remove packages (from admin powershell):
- `Remove-AppxPackage -AllUsers -Package 'Microsoft.XXXXXXXXXXXXXXXXXXXXXXXXXX'`
- `Remove-AppxPackage -Package 'Microsoft.BingWeather_XXXXXXXXXXXXXXXXXXXXXXXX'`

bloatware to remove:	
- remove Cortana
- remove OneDrive
- remove Xbox
- remove WindowsBackup
- remove Skype
- remove Game Bar: `Get-AppxPackage Microsoft.XboxGamingOverlay | Remove-AppxPackage`

---

other scripts in that field:
- https://gist.github.com/mrik23/e8160517b19a3a9dad9c1b5e8ba0fb78
