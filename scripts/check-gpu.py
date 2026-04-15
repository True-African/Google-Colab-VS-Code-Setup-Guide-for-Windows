#!/usr/bin/env python3
"""Check GPU availability in the current Colab/notebook environment."""

import subprocess
import sys


def check_gpu():
    print("=" * 50)
    print("GPU Availability Check")
    print("=" * 50)

    # nvidia-smi check
    try:
        result = subprocess.run(
            ["nvidia-smi"],
            capture_output=True,
            text=True,
            timeout=10
        )
        if result.returncode == 0:
            print("NVIDIA GPU detected via nvidia-smi:")
            print(result.stdout)
        else:
            print("nvidia-smi returned an error — no GPU available on this runtime.")
    except FileNotFoundError:
        print("nvidia-smi not found — no GPU available on this runtime.")
    except subprocess.TimeoutExpired:
        print("nvidia-smi timed out.")

    # PyTorch check
    try:
        import torch
        cuda_available = torch.cuda.is_available()
        print(f"\nPyTorch CUDA available: {cuda_available}")
        if cuda_available:
            print(f"GPU Device: {torch.cuda.get_device_name(0)}")
    except ImportError:
        print("\nPyTorch not installed in this environment.")

    # TensorFlow check
    try:
        import tensorflow as tf
        gpus = tf.config.list_physical_devices("GPU")
        print(f"\nTensorFlow GPU devices: {gpus}")
    except ImportError:
        print("TensorFlow not installed in this environment.")

    print("=" * 50)


if __name__ == "__main__":
    check_gpu()
