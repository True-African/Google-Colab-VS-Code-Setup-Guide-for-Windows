# PowerShell script - reminder to disconnect all Colab servers via VS Code
Write-Host "Disconnecting Google Colab servers..." -ForegroundColor Cyan
Write-Host ""
Write-Host "Manual steps required in VS Code:" -ForegroundColor Yellow
Write-Host "  1. Press Ctrl+Shift+P to open the command palette"
Write-Host "  2. Type 'Remove Server' and press Enter"
Write-Host "  3. Select 'colab-cpu', 'colab-gpu', or 'colab-tpu' to remove"
Write-Host "  4. Repeat for each active server"
Write-Host ""
Write-Host "Alternatively: close VS Code completely to terminate all connections." -ForegroundColor Cyan
