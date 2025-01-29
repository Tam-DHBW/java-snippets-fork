from datetime import datetime

now = datetime.now()
print("Current date and time:", now)

# Formatting the date and time
formatted = now.strftime("%Y-%m-%d %H:%M:%S")
print("Formatted:", formatted)
