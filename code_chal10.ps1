Justin H, Sierra, Geneva = Team M-n-M



# Print to the terminal screen all active processes ordered by highest CPU time consumption at the top. 
get-process | sort-object -property CPU -descending

# Print to the terminal screen all active processes ordered by highest Process Identification Number at the top.
get-process | sort-object -property ID | Sort-object

# Print to the terminal screen the top five active processes ordered by highest Working Set (WS(K)) at the top.
get-process | select-object {$_.Workingset } -first 5

# Start the process Internet Explorer (iexplore.exe) and have it open https://owasp.org/www-project-top-?ten/.
$ie = Start-process -file iexplore -arg "https://owasp.org/www-project-top-?ten/." -passthru
# Start the process Internet Explorer (iexplore.exe) ten times using a for loop. Have each instance open https://owasp.org/www-project-top-ten/.
1..10 | ForEach-Object {
    $ie = New-Object -ComObject InternetExplorer.Application
    $ie.Navigate("https://owasp.org/www-project-top-ten/")
    $ie.Visible = $true
}

# Close all Internet Explorer windows.
Get-Process iexplore | ForEach-Object {
    $_.CloseMainWindow()
}

# Kill a process by its Process Identification Number. Choose a process whose termination won't destabilize the system, such as Internet Explorer or MS Edge.
stop-process -ID 5476 -confirm -passthru
12:39
