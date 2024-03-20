#!/usr/bin/env powershell

<#
Credit:
- ChatGPT by OpenAI
  - It writes almost all code.
#>

sudo

$networkAdapterName = 'WLAN 3'  # Replace with the actual name of your Wi-Fi adapter

$networkAdapter = Get-NetAdapter | Where-Object { $_.Name -eq $networkAdapterName }

if ($networkAdapter) {
    $networkAdapter | Enable-NetAdapter -Confirm:$false
    Write-Host "Network enabled."
} else {
    Write-Host "Wi-Fi adapter '$networkAdapterName' not found."
}
