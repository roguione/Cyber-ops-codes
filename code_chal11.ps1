





- `Set-NetFirewallProfile -Profile Domain,Public -FileAndPrinterSharing Enabled`: This command enables File and Printer Sharing in both the Domain and Public firewall profiles.

- `New-NetFirewallRule -DisplayName "Allow ICMPv4-In" -Protocol ICMPv4 -IcmpType 8 -Enabled True`: This command creates a new firewall rule that allows incoming ICMP traffic (ping requests).

- `Enable-PSRemoting -Force`: This command enables remote management in PowerShell.

- `Get-AppxPackage *BloatwareName* | Remove-AppxPackage`: This command retrieves the package(s) of the specified bloatware and removes them from the system.

- `Enable-WindowsOptionalFeature -Online -FeatureName Microsoft-Hyper-V -All`: This command enables the Hyper-V feature in Windows.

- `Disable-WindowsOptionalFeature -Online -FeatureName SMB1Protocol -All`: This command disables the SMBv1 protocol, which is known to be insecure.
