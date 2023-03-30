# Justin H worked with Geneva, Sierra, and Nick A
# Auto New Users
# https://blog.netwrix.com/2018/06/07/how-to-create-new-active-directory-users-with-powershell/
# 29Mar23



# Import the ActiveDirectory module
Import-Module ActiveDirectory

# Create a new user account with the specified properties
New-ADUser -Name "Franz Ferdinand" `
  -GivenName "Franz" `
  -Surname "Fredinand" `
  -SamAccountName "Franz.F" `
  -UserPrincipalName "fredi@GlobeXpower.com" `
  -AccountPassword (Read-Host -AsSecureString "Input Password") `
  -Enabled $true

# Retrieve information about the newly created user
Get-ADUser Franz.F
