# AUTOMATE_W/BYPASS.ps1

# C:\AUTOMATE.ps1 from directory the AUTOMATE.ps1, GreenGenius.csv & GreenGenius_OU.txt are in
# For our scenario, C:\ is where we stored .ps1, OU ,and .csv
# Save this script and CSV/TXT files to C:\
# When running this script, add the phase # as an argument, In same drive as file C:\AUTOMATE.ps1 1<---- = argument, only put a 1 here

$Phase = $args[0]
if ($Phase -eq 1) {
    Write-Host "Skipping login for Phase 1..."
} elseif ($Phase -eq 2) {
    Write-Host "Skipping login for Phase 2..."
} elseif ($Phase -eq 3) {
    Write-Host "Skipping login for Phase 3..."
} else {
    Write-Host "No phase specified. Please specify a phase number as an argument."
    exit
}

Function AddRunOnceReg {
    param($val)
    # Define the path to the script file
    $cmd = "powershell.exe C:\AUTOMATION.ps1 $val" # -NoProfile -ExecutionPolicy Bypass"

    # Define the name of the registry value
    $valueName = "TEST"

    # Define the registry path for the autorun key
    $keyPath = "HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\RunOnce"

    # Create a new registry key for the autorun key
    New-ItemProperty -Path $keyPath -Name $valueName -Value "$cmd" -PropertyType String -Force | Out-Null
    Write-Host "Scheduled Phase $val for the next reboot..."
}

Function Phase1 {
    $newname = "GRNGNS-WINSVR" # new hostname
    $newip = "10.11.11.123"    # new ip address
    $newvlsm = 27              # subnet mask in slash notation
    $newgtwy = "10.11.11.126"  # new default gateway


    $adapter = Get-NetAdapter  # extract NIC index
    Write-Host "Adapter index: $($adapter[0].ifIndex)"

    # delete the existing IP address and default gateway
    write-host "Clearing the existing IP address and the default gateway, if any..."
    Remove-NetIPAddress -InterfaceIndex $($adapter[0].ifIndex) -Confirm:$false
    Remove-NetRoute -InterfaceIndex $($adapter[0].ifIndex) -Confirm:$false
    sleep(1)


    # set the static IP using the variables as inputs
    write-host "Setting the static IP address to $newip"
    New-NetIPAddress -InterfaceIndex $adapter[0].ifIndex -IPAddress $newip -PrefixLength $newvlsm -DefaultGateway $newgtwy
    sleep(1)

    # change the hostname
    write-host "Renaming this computer to $newname"
    Rename-Computer -NewName $newname
    sleep(1)

#    ipconfig
#    hostname
   }

Function Phase2 {
    $adminPassword = ConvertTo-SecureString "Password123!@#" -AsPlainText -Force

    write-host "Installing pre-requisites..."
    Install-WindowsFeature -Name AD-Domain-Services
    Import-Module ADDSDeployment

    write-host "Deploying a new Windows domain..."
    sleep(1)


    Install-ADDSForest `
    -CreateDnsDelegation:$false `
    -DatabasePath "C:\Windows\NTDS" `
    -DomainMode "WinThreshold" `
    -DomainName "corp.greengenius.com" `
    -DomainNetbiosName "GREENGENIUS" `
    -ForestMode "WinThreshold" `
    -InstallDns:$true `
    -LogPath "C:\Windows\NTDS" `
    -NoRebootOnCompletion:$false `
    -SysvolPath "C:\Windows\SYSVOL" `
    -SafeModeAdministratorPassword $adminPassword `
    -Force:$true
   }

Function Phase3 {
    Install-WindowsFeature RSAT-AD-Tools
    #Add-WindowsCapability -Name Rsat.ActiveDirectory.DS-LDA.tool~~~~0.0.1.0 -Online
    #Import-Module ActiveDirectory

    # Add OUs to AD
    $file = "C:\GreenGenius_OU.txt"
    # loop through each line
    foreach ($line in Get-Content $file) 
        {
         Write-Host "Adding the $line OU"
         New-ADOrganizationalUnit -name $line -path "DC=corp,DC=greengenius,DC=com" -ProtectedFromAccidentalDeletion:$false
        }

    # Add users to respective OUs
    $ADUser = Import-Csv "c:\GreenGenius.csv"
    $password = "Password123!@#"
    $count = 1
    foreach ($User in $ADUser) 
       {
        Write-Host "$count > Adding user $($User.firstname) $($User.lastname) to $($User.OU) OU"
        New-ADUser `
            -Name "$($User.firstname) $($User.lastname)" `
            -GivenName $User.firstname `
            -Surname $User.lastname `
            -Enabled $true `
            -Path "OU=$($User.OU),DC=corp,DC=greengenius,DC=com" `
            -Title $User.jobtitle `
            -EmailAddress $User.email `
            -AccountPassword (ConvertTo-SecureString $password -AsPlainText -Force)
        $count++
       }

   }








if (([Security.Principal.WindowsPrincipal] [Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator))
  { Write-Host "ADMIN ACCESS CHECK: OK" }
 else 
  {
   Write-Host "ADMIN ACCESS CHECK: FAIL" 
   Write-Host "Please run this script as administrator"
   Exit
  }

#Set-ExecutionPolicy Unrestricted


$phase = $args[0]

switch  ($phase) {
    "1" {
         Write-Host "Executing Phase 1..."
         #ACTUAL WORKING CODE FOR PHASE 1
         Phase1
         AddRunOnceReg -val "2"
        }
    "2" { 
         Write-Host "Executing Phase 2..."
         #ACTUAL WORKING CODE FOR PHASE 2
         Phase2
         AddRunOnceReg -val "3" 
        }
    "3" {
         Write-Host "Executing Phase 3..." 
         #ACTUAL WORKING CODE FOR PHASE 3
         Phase3
        }
    Default { Write-Host "No phase specified. Please add a phase number (1-3) as an argument. Exiting..." }
}


Write-Host "PHASE $phase COMPLETE"
write-host "Rebooting in:    (press Ctrl+C to abort)"
$countdown = 10 
while ($countdown -gt 0)
    {
     write-host "$countdown " -NoNewline
     sleep(1)
     $countdown--
    }
Restart-Computer -Force