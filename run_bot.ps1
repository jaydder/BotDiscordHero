# Script para reiniciar o bot Discord do Ragnarok
# Este script mantém o bot rodando e reinicia quando encerrar

$restartLoop = $true

while ($restartLoop) {
    Write-Host ""
    Write-Host "========================================"
    Write-Host "Iniciando Bot Discord Ragnarok..."
    Write-Host "========================================"
    Write-Host ""
    
    # Executa o bot
    python discord_bot.py
    
    Write-Host ""
    Write-Host "========================================"
    Write-Host "Bot encerrado! Aguardando 5 segundos..."
    Write-Host "========================================"
    Write-Host ""
    
    # Aguarda 5 segundos antes de reiniciar
    Start-Sleep -Seconds 5
}
