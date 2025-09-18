@echo off
REM Git hook: pre-commit (Windows). Requires PowerShell and git.exe on PATH.
powershell -ExecutionPolicy Bypass -File "%~dp0..\scripts\content_guard.ps1"
IF ERRORLEVEL 1 (
  echo [pre-commit] Content guard failed. Commit aborted.
  exit /b 1
)
