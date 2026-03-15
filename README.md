# 🛡️ NapKnight: Driver Fatigue & Distraction Monitor

NapKnight is a graphical dashboard and camera system built to detect if a driver falls asleep or looks away from the road. 

## 🚀 How to Install and Run

Because computer setups are different, please choose the installation path that matches your system.

---

### PATH A: "The Easy Way" (If you DO NOT have Python installed yet)
*Use this if this is your first time using Python on your computer.*

1. **Get Python:** Open the **Microsoft Store** on your Windows computer, search for **Python 3.12**, and click Install. *(Note: Do not install 3.13 or 3.14, as they can sometimes bug out with camera tools).*
2. **Open VS Code:** Open the NapKnight project folder inside VS Code.
3. **Open the Correct Terminal:** Go to the top menu and click **Terminal -> New Terminal**. 
   * *CRITICAL:* Make sure you are using **Command Prompt**. Beside the little `+` Click the dropdown arrow at the top right of the terminal box and select **Command Prompt**. Do NOT use PowerShell.
4. **Install AI Tools:** Inside that terminal, type this exact command and hit Enter:
   ```cmd
   pip install opencv-python numpy
5. **Run the App:** Once the download finishes, type:
   ```cmd
   python NapKnight.py
---

### PATH B: "The Safe Way" (If you ALREADY have Python 3.13 or 3.14 installed)
*Use this if you already use Python for other classes. We will use a Virtual Environment so this project doesn't mess up your other files.*
1. **Open VS Code:** Open the NapKnight project folder inside VS Code.
2. **Open the Correct Terminal:** Go to the top menu and click **Terminal -> New Terminal**. 
   * *CRITICAL:* Make sure you are using **Command Prompt**. Beside the little `+` Click the dropdown arrow at the top right of the terminal box and select **Command Prompt**. Do NOT use PowerShell.
3. **Create the Safe Box:** Type this and hit Enter:
   ```cmd
   python -m venv .venv
4. **Turn the Box On:** Type this and hit Enter:
   ```cmd
   .venv\Scripts\activate
(You should now see (.venv) appear on the far left side of your typing line).

5. **Install AI Tools:** Inside the active terminal, type:
  ```cmd
   pip install opencv-python numpy
```
6. **Run the App:** Type:
```cmd
   python NapKnight.py


