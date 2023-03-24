





# Enable File and Printer Sharing
Set-NetFirewallProfile -Profile Domain,Public -FileAndPrinterSharing Enabled

# Allow ICMP traffic
New-NetFirewallRule -DisplayName "Allow ICMPv4-In" -Protocol ICMPv4 -IcmpType 8 -Enabled True

# Enable Remote management
Enable-PSRemoting -Force

# Remove bloatware
Get-AppxPackage *BloatwareName* | Remove-AppxPackage

# Enable Hyper-V
Enable-WindowsOptionalFeature -Online -FeatureName Microsoft-Hyper-V -All

# Disable SMBv1, an insecure protocol
Disable-WindowsOptionalFeature -Online -FeatureName SMB1Protocol -All
