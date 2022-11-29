@echo off
setlocal enabledelayedexpansion

for /d %%d in (*) do (
	REM go to each directory
	cd /d %%d
	
	REM check if directory is git repository
	for /F "tokens=*" %%a in ('git rev-parse --is-inside-work-tree') do (
		set _temp=%%a
		set _result=!_temp!
		echo GIT REPO: "[32m%%d[0m"
		
		REM we could execute commands from here, because if it fails
		REM it will break loop and go through
		for /F "tokens=*" %%b in ('git config --get remote.origin.url') do (
			set _temp2=%%b
			set remote_url=!_temp2!
			echo remote_url: "[34m!remote_url![0m"
		)
	)
	
	REM go upwards
	cd ..
)
pause

REM colors:
	REM https://ss64.com/nt/syntax-ansi.html
	REM "[31mDARK_RED[0m"
	REM "[32mDARK_GREEN[0m"
	REM "[33mDARK_YELLOW[0m"
	REM "[34mDARK_BLUE[0m"
	REM "[35mDARK_MAGENTA[0m"

REM useful:
	REM https://community.notepad-plus-plus.org/topic/23004/what-did-notepad-interpret-to-result-in-an-esc-character
	
	