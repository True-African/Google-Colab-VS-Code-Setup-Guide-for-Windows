#!/usr/bin/env python3
"""Check if you're connected to a Google Colab runtime in VS Code."""

import sys
import os
import platform


def check_colab_environment():
    print("=" * 50)
    print("Google Colab Connection Checker")
    print("=" * 50)

    # Check for Colab-specific environment variables
    is_colab = "COLAB_GPU" in os.environ or "COLAB_TPU_ADDR" in os.environ

    if is_colab:
        print("Connected to Google Colab runtime!")

        if "COLAB_GPU" in os.environ:
            print(f"   GPU: {os.environ.get('COLAB_GPU', 'Unknown')}")

        if "COLAB_TPU_ADDR" in os.environ:
            print(f"   TPU Address: {os.environ['COLAB_TPU_ADDR']}")
    else:
        print("NOT connected to Google Colab")
        print("   Running on local kernel")
        print(f"   Local machine: {platform.node()}")
        print(f"   Local processor: {platform.processor()}")

    print(f"\nPython version: {sys.version}")
    print("=" * 50)
    return is_colab


if __name__ == "__main__":
    check_colab_environment()
