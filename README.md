WAVtoSpec
=======

Tools to convert WAV audio files into spectrogram images.

Files
-
- `make_spec.py`: Simple CLI script. Usage:

	```
	python make_spec.py path/to/file.wav
	```

	This reads the WAV file, computes a spectrogram, and saves an image `file_spectrogram.png` next to the WAV file.

- `audio_spectrogram_utils.py`: Same functionality as `make_spec.py` but exposes `wav_to_spectrogram_image(input_wav, output_image_path=None, show=False)` for programmatic use.

Requirements
-
- Python 3.8+
- `numpy`
- `scipy`
- `matplotlib`

Install
-
Create a virtual environment and install dependencies:

```bash
python -m venv .venv
.venv\\Scripts\\activate
pip install -r requirements.txt
```

Usage examples
-
Generate spectrogram from a WAV file:

```cmd
python make_spec.py "C:\\Users\\rusty\\Music\\wts.wav"
```

Use programmatically:

```py
from audio_spectrogram_utils import wav_to_spectrogram_image
wav_to_spectrogram_image(r"C:\\path\\to\\file.wav")
```

Notes
-
- The scripts set a non-interactive matplotlib backend (`Agg`) to ensure images are saved even when running without a display.
- If you want to view the image, open the generated `_spectrogram.png` file in any image viewer.

Short wrapper (Windows)
-
There's a short wrapper `run_wts.bat` in the repository that runs `make_spec.py` on the example `wts.wav` and opens the generated PNG automatically. From the repo folder run:

```cmd
.\run_wts.bat
```

This will generate `C:\Users\rusty\Music\wts_spectrogram.png` and then open it in your default image viewer. The same PNG is also copied into the repo as `wts_spectrogram.png` for quick preview on GitHub or in VS Code.

Opening in Explorer
-
If `start` doesn't bring the image to the foreground on your system, use Explorer to select the file instead:

```cmd
explorer /select,"C:\Users\rusty\Music\wts_spectrogram.png"
```

Generalized wrapper (PowerShell)
-
Use the PowerShell wrapper `make_spec.ps1` to generate spectrograms for any WAV file:

```powershell
.\make_spec.ps1 "C:\path\to\your\audio.wav"
```

This will:
1. Run `make_spec.py` on your WAV file
2. Generate `your_audio_spectrogram.png` in the same folder as the WAV
3. Open the PNG in your default image viewer automatically

Examples:

```powershell
.\make_spec.ps1 "C:\Users\rusty\Music\wts.wav"
.\make_spec.ps1 "C:\Users\rusty\Music\song.wav"
.\make_spec.ps1 "D:\recordings\podcast.wav"
```

The wrapper validates that the WAV file exists before running and reports any errors clearly.

License
-
Add your preferred license here.
