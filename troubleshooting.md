# Troubleshooting Guide

## Common Issues and Solutions

---

### Issue: "Colab" option doesn't appear in kernel source list

**Solution:**
- Ensure **both** Jupyter AND Colab extensions are installed
- Restart VS Code completely (`Ctrl+Shift+P` → `Developer: Reload Window`)
- Verify the Colab extension publisher is **Google** (not a third-party clone)

---

### Issue: Authentication fails

**Solution:**
- Clear your browser cache and cookies
- Try in an incognito/private browser window
- Ensure pop-ups are not blocked for `accounts.google.com`
- Reinstall the Colab extension: uninstall → restart VS Code → reinstall

---

### Issue: GPU not showing (`nvidia-smi: command not found`)

**Cause:** You connected via **Auto Connect**, which gives CPU only.

**Solution:**
- Do **not** use "Auto Connect" for GPU
- Use: kernel selector → **Colab** → **New Colab Server** → **GPU** → **T4**
- Wait 2–3 minutes for GPU allocation to complete

---

### Issue: Runtime disconnects unexpectedly

**Solution:**
- Free Colab runtimes have a ~12-hour session limit
- Reconnect using the same method (New Colab Server → GPU → T4)
- Consider Colab Pro for longer, more stable sessions

---

### Issue: Cannot remove server from command palette

**Solution:**
- Close all open notebook tabs first
- Run `Developer: Reload Window` from the command palette
- Try the Remove Server command again
- As a last resort, close VS Code entirely to terminate all connections

---

### Issue: Authorization code input disappears before you can paste

**Solution:**
- Copy the code from the browser first, then click the VS Code window
- The input box is transient — paste immediately after it appears
- If missed, re-run the connection flow from the kernel selector

---

### Issue: `import torch` or `import tensorflow` fails

**Solution:**
- Libraries are pre-installed in Colab but may need runtime restart
- Run `!pip install torch` in a cell if still missing
- Ensure you selected a GPU runtime (some packages behave differently on CPU)

---

## Verification Checklist

Run the [check-colab-connection.py](scripts/check-colab-connection.py) script to diagnose your environment, or manually verify:

1. ✅ Jupyter extension installed (by Microsoft)
2. ✅ Colab extension installed (by Google)
3. ✅ Kernel shows `/usr/bin/python3 (Colab)` when connected
4. ✅ `!nvidia-smi` shows Tesla T4 when on GPU runtime
5. ✅ Basic cell execution runs in under 1 second

---

## Still Having Issues?

1. Check the VS Code **Output** panel → select **"Jupyter"** from the dropdown
2. Open an issue in this repository with:
   - Your Windows version
   - VS Code version
   - Error message (copy from Output panel)
   - Steps that led to the problem
