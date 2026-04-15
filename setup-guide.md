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

1. Press `Ctrl+Shift+X` to open the Extensions panel — click the **grid icon** in the left sidebar

   ![VS Code activity bar with the Extensions grid icon circled](<Last 12 images/image-1776284728850.png>)

2. Search for **"Jupyter"**

   ![Extensions Marketplace searching for "jupyter"](<Last 12 images/image-1776284794242.png>)

3. Click the **Jupyter** extension by Microsoft (98M+ downloads)

   ![Jupyter extension in search results showing 98M downloads and Install button](<Last 12 images/image-1776284892969.png>)

4. Click **Install** on the extension detail page

   ![Jupyter extension detail page with Install button highlighted](<Last 12 images/image-1776284926916.png>)

> The Jupyter extension is a required prerequisite for the Colab extension to work.

---

## Step 2: Install the Google Colab Extension

1. In the Extensions panel, search for **"Colab"**

   ![Extensions Marketplace searching for "colab" showing Colab by Google](<Last 12 images/image-1776284955806.png>)

2. Click the **Colab** extension — **Important:** confirm the publisher is **Google** (verified blue checkmark)

   ![Colab extension detail page showing Google as verified publisher with Install button](<Last 12 images/image-1776284990928.png>)

3. Click **Install**, then click **"Trust Publisher & Install"** when prompted

   !["Do you trust the publisher Google?" dialog with Trust Publisher & Install button circled](<Last 12 images/image-1776285047290.png>)

> Always verify the publisher is Google before installing to avoid unofficial clones.

---

## Step 3: Create a Jupyter Notebook

1. In the Explorer panel (`Ctrl+Shift+E`), right-click and create a new file named `test.ipynb`

   ![VS Code Explorer panel with test.ipynb highlighted and arrows pointing to it](<Last 12 images/image-1776285131260.png>)

2. VS Code recognizes it as a Jupyter notebook — you'll see the **Colab** button appear in the toolbar

   ![test.ipynb open in VS Code showing the Colab button in the notebook toolbar](<Last 12 images/image-1776285323178.png>)

3. Add a code cell (click **+ Code**) and type something — the notebook is ready to connect

   ![test.ipynb with a code cell showing import pandas as pd](<Last 12 images/image-1776284568422.png>)

---

## Step 4: Connect to Google Colab

### Option A: Auto-connect (CPU only)

1. Click the **"Python 3 (ipykernel)"** kernel selector in the top-right of the notebook

   ![Close-up of the Python 3 (ipykernel) kernel selector button](<Last 12 images/image-1776285351122.png>)

2. A dropdown appears — select **"Select Another Kernel..."**

   ![Change kernel dropdown: Python 3 Currently Selected and Select Another Kernel option](<Last 12 images/image-1776285381380.png>)

3. Choose **"Colab"** from the kernel source list

   ![Kernel source picker: Python Environments, Jupyter Kernel, Existing Jupyter Server, and Colab](<Last 12 images/image-1776285399597.png>)

4. Click **"Auto Connect"** to connect instantly to a CPU runtime

   ![Select a remote server: Auto Connect, New Colab Server, Open Colab Web](<Last 12 images/image-1776285457923.png>)

5. **Sign in with your Google account** — follow these steps exactly:

   a. VS Code asks: *"The extension 'Colab' wants to sign in using Google"* — click **Allow**

   !["The extension Colab wants to sign in using Google" dialog with Allow button](<Last 12 images/image-1776285475959.png>)

   b. VS Code asks to open an external website — click **Open**

   !["Do you want Code to open the external website?" dialog showing accounts.google.com URL with Open button](<Last 12 images/image-1776285516936.png>)

   c. The Google authorization page opens in your browser — click the **copy icon** to copy the code

   ![Google Colab authorization page with "Copy the code" section and copy icon circled](<Last 12 images/image-1776285570683.png>)

   d. Back in VS Code, an input box appears — paste the code and press **Enter**

   ![VS Code authorization code input box: "Enter your authorization code (Press Enter to confirm)"](<Last 12 images/image-1776285627537.png>)

   ![VS Code authorization code input with the code pasted (shown as dots)](<Last 12 images/image-1776285653230.png>)

   e. The kernel picker reappears — select **Python 3 (ipykernel)**

   ![Kernel picker showing Python 3 (ipykernel) Recommended, Julia, R](<Last 12 images/image-1776285675134.png>)

---

### Option B: GPU/TPU Connection ⭐ (Recommended for ML)

1. Follow steps 1–4 from Option A above to reach the remote server picker
2. Select **"New Colab Server"** instead of Auto Connect

   ![Select a remote server options including New Colab Server with description "CPU, GPU or TPU"](<Last 12 images/image-1776286001542.png>)

3. Choose your runtime type — select **GPU** for machine learning workloads

   ![Runtime selection showing CPU, GPU (cursor on GPU), and TPU options](<Last 12 images/image-1776286029004.png>)

4. Select **T4** as the GPU type (free tier)

   ![T4 GPU type selection](<Last 12 images/image-1776286049421.png>)

5. Select **Python 3 (ipykernel)** as the notebook kernel

   ![Kernel list showing Julia 1.11, Python 3 (ipykernel) highlighted, and R](<Last 12 images/image-1776286097833.png>)

6. Complete Google sign-in (same steps as Option A, step 5 above)

---

## Step 5: Verify Your Connection

Once connected, the kernel selector in the top-right changes to show `Python 3 (ipykernel) /usr/bin/python3 (Colab)`:

![Notebook top-right showing the Colab runtime kernel name](<Last 12 images/image-1776285847029.png>)

You can also confirm by clicking the kernel — it shows **Colab** as the currently selected source:

![Change kernel dialog showing "Python 3 /usr/bin/python3 (Colab) — Currently Selected"](<Last 12 images/image-1776285881237.png>)

The notebook toolbar also displays the **Colab** button, confirming the active connection:

![Notebook toolbar with Colab button visible and the + Code button highlighted](<Last 12 images/image-1776285730630.png>)

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

  ![!nvidia-smi cell output with GPU utilization and process table](<Last 12 images/image-1776284603912.png>)

---

## Step 6: Switch Between Runtimes

To switch from CPU to GPU (or vice versa):

1. Click the kernel name in the top-right of the notebook
2. Select **"Select Another Kernel..."**
3. Choose **"Colab"** from the kernel source list

   ![Kernel source picker with Colab highlighted/circled](<Last 12 images/image-1776285940519.png>)

4. Choose **"New Colab Server"** → pick the new runtime type
5. Sign in again if required

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
