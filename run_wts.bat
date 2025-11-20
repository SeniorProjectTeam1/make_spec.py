@echo off
REM Run make_spec for the default wts.wav in the user's Music folder
python "%~dp0\make_spec.py" "C:\Users\rusty\Music\wts.wav"

REM Open the generated spectrogram in the default image viewer
start "" "C:\Users\rusty\Music\wts_spectrogram.png"
