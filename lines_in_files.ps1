$files = Get-ChildItem *.txt
foreach ($file in $files) {
    'file: {0}, lines: {1}' -f $file.name, (type $file | Measure-Object -line ).Lines
    }
    
echo "`n"
Write-Host -NoNewLine 'Press any key to continue...';
$null = $Host.UI.RawUI.ReadKey('NoEcho,IncludeKeyDown');