import os
import sys

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import scipy.io.wavfile as siow
from scipy import signal


def wav_to_spectrogram_image(input_wav, output_image_path=None, show=False):
    # ---- load wav ----
    sampling_rate, data = siow.read(input_wav)

    # stereo → mono
    if data.ndim > 1:
        amplitude_vector = data.mean(axis=1)
    else:
        amplitude_vector = data

    amplitude_vector = amplitude_vector.astype(np.float32)
    wav_length = amplitude_vector.shape[0] / sampling_rate
    print(f"Loaded {input_wav}")
    print(f"Sampling rate: {sampling_rate} Hz")
    print(f"Length: {wav_length:.3f} seconds")

    # ---- spectrogram ----
    freqs, times, S = signal.spectrogram(
        amplitude_vector,
        fs=sampling_rate,
        nperseg=1024,
        noverlap=512,
        scaling="spectrum",
        mode="magnitude",
    )

    # log scale for better visibility
    S = np.maximum(S, 1e-10)
    S = 20 * np.log10(S)

    # ---- output path ----
    if output_image_path is None:
        base, _ = os.path.splitext(input_wav)
        output_image_path = base + "_spectrogram.png"

    # ---- save image ----
    plt.figure(figsize=(10, 4))
    plt.imshow(
        S,
        aspect="auto",
        origin="lower",
        extent=[times.min(), times.max(), freqs.min(), freqs.max()],
    )
    plt.ylabel("Frequency [Hz]")
    plt.xlabel("Time [s]")
    plt.colorbar(label="Magnitude (dB)")
    plt.tight_layout()
    plt.savefig(output_image_path, bbox_inches="tight", pad_inches=0)
    if show:
        plt.show()
    else:
        plt.close()

    print(f"Saved spectrogram image to: {output_image_path}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python audio_spectrogram_utils.py path/to/file.wav")
        sys.exit(1)

    input_wav = sys.argv[1]
    wav_to_spectrogram_image(input_wav, show=True)
