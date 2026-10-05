@echo off
cd /d "%~dp0"
where py >nul 2>nul
if %errorlevel%==0 (
  start "" py app.py
  exit /b
)
where python >nul 2>nul
if %errorlevel%==0 (
  start "" python app.py
  exit /b
)
echo.
echo ERRO: Python nao foi encontrado neste computador.
echo O painel ainda pode ser aberto pelo index.html com os dados locais.
echo Para edicao local automatica, instale o Python 3.
pause
