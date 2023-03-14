$begin = get-date -date "02/16/2023 08:00:00"
$End = Get-date -date "02/16/2023 14:00:00"

# Main

#Output all events in 24 to last_24.txt
Get-eventlog -logname system -after $begin -before $end | Outfile C:\test\last_24.txt

#export error codes in a file named error.txt
Get-eventlog -logname system -entrytype error | outfile C:\test\error.txt

#Print to the screen all events with ID of 16
Get-eventlog -logname system -InstanceID 16

#Print to the screen the most recent 20 entries
Get-eventlog -logname system -newest 20

#Print to the screen the most recent 500 entries
Get-eventlog -logname system -newest 500

#end
