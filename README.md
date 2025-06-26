
# Python Virtual Environment Setup (Windows)

This guide helps you set up and activate a Python virtual environment on a Windows system.

## 🛠 Prerequisites

* Python 3.6+ installed on your system
  You can verify by running:

```bash
python --version
```

Make sure Python and `pip` are added to your system PATH.

---

## 📦 Create a Virtual Environment

1. Open **Command Prompt (cmd)** or **PowerShell**
2. Navigate to your project directory:

```bash
cd path\to\your\project
```

3. Create a virtual environment named `venv`:

```bash
python -m venv venv
```

This will create a folder named `venv` in your project directory.

---

## 🚀 Activate the Virtual Environment

### Using Command Prompt (cmd):

```bash
venv\Scripts\activate.bat
```

### Using PowerShell:

```bash
venv\Scripts\Activate.ps1
```

> ⚠️ If you get a *"running scripts is disabled"* error in PowerShell, run this (once, as Admin):

```bash
Set-ExecutionPolicy RemoteSigned
```

---

## 🧪 Verify Activation

Once activated, you should see the virtual environment name in the terminal prompt, like this:

```bash
(venv) C:\your\project\path>
```

---

## 📥 Install Dependencies

After activation, install packages as usual using `pip`:

```bash
pip install -r requirements.txt
```

Or install packages manually:

```bash
pip install flask  # example
```

---

## ❌ Deactivate the Virtual Environment

To deactivate the environment when you're done:

```bash
deactivate
```

---

## 📌 Notes

* Always activate the virtual environment before running your Python code.


