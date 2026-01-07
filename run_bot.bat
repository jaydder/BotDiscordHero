@echo off
REM Script para reiniciar o bot Discord do Ragnarok
REM Este script mantém o bot rodando e reinicia quando encerrar

:restart_loop
echo.
echo ========================================
echo Iniciando Bot Discord Ragnarok...
echo ========================================
echo.

python discord_bot.py

echo.
echo ========================================
echo Bot encerrado! Aguardando 5 segundos antes de reiniciar...
echo ========================================
echo.

timeout /t 5 /nobreak

goto restart_loop
