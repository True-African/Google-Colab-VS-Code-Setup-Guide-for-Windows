# Complete Setup Guide: Google Colab + VS Code on Windows

## Overview

This guide walks you through connecting VS Code to Google Colab's cloud runtimes, giving you access to free GPUs and TPUs directly from your local editor.

---

## Prerequisites

- VS Code installed on Windows
- Google account (free)
- Internet connection

---

## Step 1: Install the Jupyter Extension

1. Press `Ctrl+Shift+X` to open the Extensions panel — click the grid icon in the left sidebar
2. Search for **"Jupyter"**
3. Install the official **Jupyter** extension by Microsoft (98M+ downloads)

> The Jupyter extension is a required prerequisite for the Colab extension to work.

---

## Step 2: Install the Google Colab Extension

1. In the Extensions panel, search for **"Colab"**
2. **Important:** Ensure the publisher is **Google** (verified blue checkmark)
3. Click **Install**
4. When prompted, click **"Trust Publisher & Install"**

> Always verify the publisher is Google before installing to avoid unofficial clones.

---

## Step 3: Create a Jupyter Notebook

1. In the Explorer panel, create a new file: `test.ipynb`
2. VS Code will automatically recognize it as a Jupyter notebook
3. You should see the **Colab** button appear in the notebook toolbar

![Notebook opened in VS Code showing the Colab button in the toolbar](<Last 12 images/image-1776285730630.png>)

---

## Step 4: Connect to Google Colab

### Option A: Auto-connect (CPU only)

1. Click the **"Python 3 (ipykernel)"** kernel selector in the top-right of the notebook

   ![Python 3 kernel picker — click to change runtime](<Last 12 images/image-1776285675134.png>)

2. The kernel change panel opens — select **"Select Another Kernel..."**

   ![Change kernel dialog showing Colab currently selected with Select Another Kernel option](<Last 12 images/image-1776285881237.png>)

3. Choose **"Colab"** from the kernel source list

   ![Kernel source picker with Python Environments, Jupyter Kernel, Existing Jupyter Server, and Colab options](<Last 12 images/image-1776285940519.png>)

4. Click **"Auto Connect"** to connect instantly to a CPU runtime

   ![Auto Connect, New Colab Server, Open Colab Web, and Upgrade to Pro options](<Last 12 images/image-1776286001542.png>)

5. Sign in with your Google account when prompted:
   - Click **Allow** when Colab asks to sign in via Google
   - Click **Open** when VS Code asks to open the external website
   - On the Google authorization page, click the **copy icon** to copy the authorization code
   - Paste the code into the VS Code input box and press **Enter**

---

### Option B: GPU/TPU Connection ⭐ (Recommended for ML)

1. Follow steps 1–3 from Option A above to reach the Colab kernel source picker
2. Select **"New Colab Server"** (see the options in the image above)
3. Choose your runtime type — select **GPU** for machine learning workloads

   ![Runtime selection showing CPU, GPU (cursor on GPU), and TPU options](<Last 12 images/image-1776286029004.png>)

4. Select **T4** as the GPU type (free tier)

   ![T4 GPU type selection](<Last 12 images/image-1776286049421.png>)

5. Select **Python 3 (ipykernel)** as the notebook kernel

   ![Kernel list showing Julia 1.11, Python 3 (ipykernel) highlighted, and R](<Last 12 images/image-1776286097833.png>)

6. Complete Google sign-in (same steps as Option A, step 5 above)

---

## Step 5: Verify Your Connection

Once connected, the top-right corner of the notebook shows `Python 3 (ipykernel) /usr/bin/python3 (Colab)`:

![Notebook top-right showing the Colab runtime kernel name](<Last 12 images/image-1776285847029.png>)

### Test with a code cell

Add a code cell and run:

```python
import pandas as pd
print("Connected to Colab!")
```

A successful execution shows a green tick and runtime in seconds:

![import pandas as pd executed successfully showing ✓ 0.3s](<Last 12 images/image-1776285779339.png>)

### Check your GPU

```python
!nvidia-smi
```

- On a **CPU runtime**: you'll see `nvidia-smi: command not found`

  ![!nvidia-smi showing "nvidia-smi: command not found" on CPU runtime](<Last 12 images/image-1776285796577.png>)

- On a **GPU runtime**: you'll see full Tesla T4 details

  ![!nvidia-smi output showing Tesla T4 GPU, CUDA 13.0, 15360MiB memory](<Last 12 images/image-1776286166302.png>)

---

## Step 6: Switch Between Runtimes

To switch from CPU to GPU (or vice versa):

1. Click the kernel name in the top-right of the notebook
2. Select **"Select Another Kernel..."**
3. Choose **"Colab"** → **"New Colab Server"** → pick the new runtime type
4. Sign in again if required

---

## Step 7: Proper Cleanup (Important!)

Always disconnect when done to free Colab resources:

1. Press `Ctrl+Shift+P` to open the command palette
2. Type **"Colab"**
3. Select **"Remove Server"**
4. Choose which server to remove: `colab-cpu`, `colab-gpu`, or `colab-tpu`
5. Verify disconnection — running a cell should fail

---

## Keyboard Shortcuts Reference

| Action                  | Shortcut        |
|-------------------------|-----------------|
| Open Extensions panel   | `Ctrl+Shift+X`  |
| Open command palette    | `Ctrl+Shift+P`  |
| Run cell                | `Shift+Enter`   |
| Add code cell           | `B`             |
| Delete cell             | `DD`            |

---

## When to Use Colab vs Local

| Use Colab Extension     | Use Local Kernel         |
|-------------------------|--------------------------|
| Training ML models      | Editing config files     |
| Running on battery      | Heavy data processing    |
| Testing GPU code        | Working offline          |
| Sharing notebooks       | Large local datasets     |
