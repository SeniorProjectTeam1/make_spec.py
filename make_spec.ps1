# PowerShell wrapper to generate spectrograms for any WAV file
# Usage: .\make_spec.ps1 "C:\path\to\audio.wav"

param(
    [Parameter(Mandatory=$true)]
    [string]$WavFile
)

# Verify the WAV file exists
if (-not (Test-Path $WavFile)) {
    Write-Error "File not found: $WavFile"
    exit 1
}

# Get the directory where this script is located
$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path

# Run make_spec.py with the provided WAV file
Write-Host "Generating spectrogram for: $WavFile"
& python "$scriptDir\make_spec.py" $WavFile

if ($LASTEXITCODE -ne 0) {
    Write-Error "Failed to generate spectrogram"
    exit 1
}

# Determine the output PNG path (same as input but with _spectrogram.png suffix)
$baseName = [System.IO.Path]::GetFileNameWithoutExtension($WavFile)
$outputDir = Split-Path -Parent $WavFile
$pngFile = Join-Path $outputDir "$baseName`_spectrogram.png"

# Open the generated PNG in the default image viewer
if (Test-Path $pngFile) {
    Write-Host "Opening: $pngFile"
    Start-Process $pngFile
} else {
    Write-Error "Spectrogram file not found: $pngFile"
    exit 1
}
