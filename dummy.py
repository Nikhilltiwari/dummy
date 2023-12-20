import pandas as pd

# Data
data = {
    "Seriousness": ["High", "Medium", "Low", "High", "Low", "Medium", "High", "Low", "Medium", "High", "Low", "Medium", "High", "Low", "Medium", "High", "Low", "Medium", "High", "Low", "Medium", "High", "Low", "Medium", "High", "Low", "Medium", "High", "Low", "Medium", "High", "Low", "Medium", "High", "Low", "Medium"],
    "Problem": ["Network connectivity", "Software compatibility", "Battery draining quickly", "System overheating", "Slow computer performance", "Data loss", "Virus infection", "Printer not working", "Application crashes", "Security breach", "Bluetooth connectivity", "Email not syncing", "Hard drive failure", "Keyboard malfunction", "Inconsistent Wi-Fi signal", "Operating system crash", "Screen brightness fluctuating", "Printer low on ink", "Unauthorized access attempts", "Mouse not responding", "Slow internet speed", "Corrupted system files", "No sound from speakers", "Webcam not functioning", "Continuous software crashes", "Mobile app not updating", "Syncing issues with cloud storage", "Electrical surges causing damage", "Inaccurate touchpad response", "Frequent browser crashes", "Loss of critical data", "External drive not recognized", "Computer fan noise", "Ransomware attack", "Difficulty connecting to VPN", "Frequent system notifications"],
    "Solution": ["Reboot router", "Update software", "Check for background apps", "Clean the cooling system", "Remove unnecessary files", "Backup data regularly", "Run antivirus scan", "Check for paper jams", "Reinstall the application", "Change passwords", "Check device compatibility", "Update email settings", "Replace the hard drive", "Clean or replace the keyboard", "Relocate router or use a Wi-Fi extender", "Reinstall the operating system", "Adjust screen settings", "Replace or refill ink cartridges", "Strengthen firewall settings", "Replace batteries or reconnect mouse", "Reset or upgrade internet plan", "Perform a system restore", "Check audio settings and connections", "Update webcam drivers", "Check for system hardware issues", "Clear app cache or update manually", "Check account settings and connectivity", "Use surge protectors", "Calibrate or replace the touchpad", "Clear browser cache or reinstall", "Implement robust data recovery plan", "Check drive connections and format", "Clean fans or replace if faulty", "Disconnect from network and consult expert", "Reconfigure VPN settings", "Adjust notification settings"]
}

# Creating DataFrame
df = pd.DataFrame(data)

# Save DataFrame to CSV file
df.to_csv("recommendations.csv", index=False)
