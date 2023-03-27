#!/usr/bin/env python3

# Script: Ops 301 ops chal-08
# Author: Justin H
# Date of latest revision: 3/27/23
# Purpose: PSUTIL
# Team: Geneva, Nick, && Sierra

"""
This script fetches system information using the Psutil module and saves it to a file on the desktop.

The following system information is fetched:
- Time spent by normal processes executing in user mode
- Time spent by processes executing in kernel mode
- Time when system was idle
- Time spent by priority processes executing in user mode
- Time spent waiting for I/O to complete
- Time spent for servicing hardware interrupts
- Time spent for servicing software interrupts
- Time spent by other operating systems running in a virtualized environment
- Time spent running a virtual CPU for guest operating systems under the control of the Linux kernel
"""

import os
import psutil

# Get the path to the user's desktop directory
desktop_path = os.path.join(os.path.expanduser('~'), 'Desktop')

# Create a file to store the system information
filename = 'system_info.txt'
file_path = os.path.join(desktop_path, filename)

# Open the file for writing
with open(file_path, 'w') as f:
    # Write the system information to the file
    f.write(f"Time spent by normal processes executing in user mode: {psutil.cpu_times().user}\n")
    f.write(f"Time spent by processes executing in kernel mode: {psutil.cpu_times().system}\n")
    f.write(f"Time when system was idle: {psutil.cpu_times().idle}\n")
    f.write(f"Time spent by priority processes executing in user mode: {psutil.cpu_times().nice}\n")
    f.write(f"Time spent waiting for I/O to complete: {psutil.cpu_times().iowait}\n")
    f.write(f"Time spent for servicing hardware interrupts: {psutil.cpu_times().irq}\n")
    f.write(f"Time spent for servicing software interrupts: {psutil.cpu_times().softirq}\n")
    f.write(f"Time spent by other operating systems running in a virtualized environment: {psutil.cpu_times().steal}\n")
    f.write(f"Time spent running a virtual CPU for guest operating systems under the control of the Linux kernel: {psutil.cpu_times().guest}\n")

print(f"System information saved to {file_path}")


