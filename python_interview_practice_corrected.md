# Python Interview Practice -- 50 DevOps Questions with Corrected Solutions

This document contains 50 commonly asked Python coding and scripting
questions for DevOps Engineer interviews. Each question includes a
working example, sample output, and a brief explanation.

**Environment note:** Linux-specific examples are marked where relevant.
Some examples require third-party packages such as `psutil`, `requests`,
`paramiko`, `boto3`, or the Kubernetes Python client. Run destructive
operations only after checking the target path and testing in a safe
environment.

# 1. Basic Python scripting

## 1. Reverse a string

``` python
text = "hello"
print(text[::-1])
```

**Output:**

``` text
olleh
```

**Explanation:** `[::-1]` uses a step of `-1`, reading the string from
right to left.

## 2. Find duplicate elements in a list

``` python
numbers = [1, 2, 3, 2, 4, 5, 3, 6]
duplicates = []
seen = set()

for num in numbers:
    if num in seen and num not in duplicates:
        duplicates.append(num)
    seen.add(num)

print(duplicates)
```

**Output:**

``` text
[2, 3]
```

**Explanation:** `seen` tracks values already encountered. A value is a
duplicate when it is already in `seen`. The result list keeps each
duplicate only once and preserves the order in which duplicates are
first detected.

## 3. Find the second-largest number in a list

``` python
numbers = [10, 25, 5, 40, 30]

greatest = float("-inf")
second = float("-inf")

for num in numbers:
    if num > greatest:
        second = greatest
        greatest = num
    elif num > second and num != greatest:
        second = num

if second == float("-inf"):
    print("There is no second-largest distinct number")
else:
    print(second)
```

**Output:**

``` text
30
```

**Explanation:** `greatest` and `second` track the largest and
second-largest distinct values found so far. Negative infinity allows
the logic to work when all numbers are negative.

**Note:** This finds the second-largest distinct value. For
`[10, 10, 8]`, the answer is `8`.

## 4. Check whether a string is a palindrome

``` python
text = "madam"

if text == text[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")
```

**Output:**

``` text
Palindrome
```

**Explanation:** A palindrome reads the same forward and backward. This
simple version is case-sensitive and includes spaces and punctuation in
the comparison.

## 5. Count the occurrence of each character in a string

``` python
text = "Welcome to python"
frequency = {}

for char in text:
    if char in frequency:
        frequency[char] += 1
    else:
        frequency[char] = 1

print(frequency)
```

**Output:**

``` text
{'W': 1, 'e': 2, 'l': 1, 'c': 1, 'o': 3, 'm': 1, ' ': 2, 't': 1, 'p': 1, 'y': 1, 'h': 1, 'n': 1}
```

**Explanation:** The dictionary stores each character as a key and its
count as the value. This counts spaces and treats uppercase and
lowercase letters as different characters.

## 6. Remove duplicates from a list

``` python
numbers = [1, 2, 3, 2, 4, 5, 3, 6]
unique_numbers = []

for num in numbers:
    if num not in unique_numbers:
        unique_numbers.append(num)

print(unique_numbers)
```

**Output:**

``` text
[1, 2, 3, 4, 5, 6]
```

**Explanation:** Add an element only if it is not already in the result
list. This preserves the original order.

## 7. Find the factorial of a number

``` python
number = 5
factorial = 1

if number < 0:
    print("Factorial is not defined for negative integers")
else:
    for i in range(1, number + 1):
        factorial *= i
    print(factorial)
```

**Output:**

``` text
120
```

**Explanation:** Factorial multiplies all positive integers from `1`
through the given number. The initial value is `1`, so `0!` is also
correctly calculated as `1`.

## 8. Print the Fibonacci series

``` python
number = 10
a = 0
b = 1

for _ in range(number):
    print(a, end=" ")
    a, b = b, a + b
```

**Output:**

``` text
0 1 1 2 3 5 8 13 21 34
```

**Explanation:** Each Fibonacci number is the sum of the previous two.
Tuple assignment updates both variables in one statement.

## 9. Check whether a number is prime

``` python
number = 7

if number <= 1:
    print("Not Prime")
else:
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            print("Not Prime")
            break
    else:
        print("Prime")
```

**Output:**

``` text
Prime
```

**Explanation:** A prime number is greater than `1` and has no positive
divisors other than `1` and itself. It is sufficient to test divisors up
to the square root. The `for-else` block runs only if the loop does not
encounter `break`.

## 10. Sort a dictionary by values

``` python
scores = {"Alice": 82, "Bob": 95, "Charlie": 78}

sorted_scores = dict(
    sorted(scores.items(), key=lambda item: item[1])
)

print(sorted_scores)
```

**Output:**

``` text
{'Charlie': 78, 'Alice': 82, 'Bob': 95}
```

**Explanation:** `items()` provides key-value pairs. The `key` function
sorts those pairs by their value (`item[1]`). Use `reverse=True` for
descending order.

# 2. Linux and system monitoring

## 11. Check whether a server is reachable

``` python
import subprocess

server = "192.0.2.10"

result = subprocess.run(
    ["ping", "-c", "2", "-W", "2", server],
    stdout=subprocess.DEVNULL,
    stderr=subprocess.DEVNULL
)

if result.returncode == 0:
    print(f"{server} is reachable")
else:
    print(f"{server} is not reachable")
```

**Output (example):**

``` text
192.0.2.10 is reachable
```

**Explanation:** `subprocess.run()` executes the system `ping` command.
A return code of `0` usually indicates success. The example uses a
documentation-only IP address; replace it with a host you are authorized
to test.

**Note:** ICMP may be blocked by a firewall even when the server is
running. A TCP health check may be more appropriate for an application.

## 12. Check CPU utilization

``` python
import psutil

cpu_usage = psutil.cpu_percent(interval=1)

print(f"CPU Usage: {cpu_usage}%")

if cpu_usage > 80:
    print("WARNING: High CPU utilization")
else:
    print("CPU utilization is normal")
```

**Output (example):**

``` text
CPU Usage: 24.5%
CPU utilization is normal
```

**Explanation:** `psutil.cpu_percent(interval=1)` measures CPU
utilization over a one-second interval.

**Requirement:** Install the package with
`python -m pip install psutil`.

## 13. Check memory utilization

``` python
import psutil

memory = psutil.virtual_memory()

print(f"Total Memory: {memory.total / (1024 ** 3):.2f} GB")
print(f"Used Memory: {memory.used / (1024 ** 3):.2f} GB")
print(f"Memory Usage: {memory.percent}%")

if memory.percent > 80:
    print("WARNING: High memory utilization")
```

**Output (example):**

``` text
Total Memory: 15.50 GB
Used Memory: 8.20 GB
Memory Usage: 52.9%
```

**Explanation:** `virtual_memory()` returns memory statistics. Dividing
bytes by `1024 ** 3` converts them to GiB (often informally called GB).

## 14. Check disk utilization

``` python
import shutil

path = "/"

usage = shutil.disk_usage(path)

total = usage.total / (1024 ** 3)
used = usage.used / (1024 ** 3)
free = usage.free / (1024 ** 3)
percentage = (usage.used / usage.total) * 100

print(f"Total Space: {total:.2f} GB")
print(f"Used Space: {used:.2f} GB")
print(f"Free Space: {free:.2f} GB")
print(f"Disk Usage: {percentage:.2f}%")

if percentage > 80:
    print("WARNING: Disk usage is high")
```

**Output (example):**

``` text
Total Space: 100.00 GB
Used Space: 65.00 GB
Free Space: 35.00 GB
Disk Usage: 65.00%
```

**Explanation:** `shutil.disk_usage()` returns total, used, and free
bytes for the filesystem containing the specified path. Change `/` to
the mount point you want to monitor.

## 15. Monitor whether a process is running

``` python
import psutil

process_name = "sshd"
found = False

for process in psutil.process_iter(["name", "pid"]):
    if process.info["name"] == process_name:
        print(f"{process_name} is running with PID {process.info['pid']}")
        found = True

if not found:
    print(f"{process_name} is not running")
```

**Output (example):**

``` text
sshd is running with PID 812
```

**Explanation:** `process_iter()` safely iterates over process
information. Process names differ across operating systems and
distributions; on some systems the SSH daemon may be named `ssh`.

## 16. Check whether a systemd service is running

``` python
import subprocess

service = "nginx"

result = subprocess.run(
    ["systemctl", "is-active", service],
    capture_output=True,
    text=True
)

if result.returncode == 0 and result.stdout.strip() == "active":
    print(f"{service} is running")
else:
    print(f"{service} is not active")
```

**Output (example):**

``` text
nginx is running
```

**Explanation:** `systemctl is-active` checks a systemd service. This
example checks status only; it does not attempt to restart the service.

## 17. Find files older than 7 days

``` python
import os
import time

directory = "/var/log"
cutoff_seconds = 7 * 24 * 60 * 60
now = time.time()

for root, _, files in os.walk(directory):
    for filename in files:
        path = os.path.join(root, filename)

        try:
            age_seconds = now - os.path.getmtime(path)
            if age_seconds > cutoff_seconds:
                print(f"Older than 7 days: {path}")
        except OSError as error:
            print(f"Could not inspect {path}: {error}")
```

**Output (example):**

``` text
Older than 7 days: /var/log/old-app.log
```

**Explanation:** `os.walk()` searches recursively. `getmtime()` returns
the last modification time as a timestamp. Subtracting it from the
current time gives the file age in seconds.

## 18. Delete files older than 30 days

``` python
import os
import time

directory = "/var/log/myapp"
cutoff_seconds = 30 * 24 * 60 * 60
now = time.time()

for root, _, files in os.walk(directory):
    for filename in files:
        path = os.path.join(root, filename)

        try:
            if now - os.path.getmtime(path) > cutoff_seconds:
                print(f"Deleting: {path}")
                os.remove(path)
        except OSError as error:
            print(f"Could not process {path}: {error}")
```

**Output (example):**

``` text
Deleting: /var/log/myapp/archive-2025-01-01.log
```

**Explanation:** The script compares each file's modification time with
a 30-day threshold and removes older files.

**Safety note:** Deletion is irreversible. First replace
`os.remove(path)` with a print statement, verify the exact files, and
use a narrowly scoped directory. This example deletes files, not
directories.

## 19. Find ERROR messages in a log file

``` python
filename = "app.log"
error_count = 0

with open(filename, "r", encoding="utf-8", errors="replace") as file:
    for line_number, line in enumerate(file, start=1):
        if "ERROR" in line:
            error_count += 1
            print(f"Line {line_number}: {line.rstrip()}")

print(f"Total errors: {error_count}")
```

**Output (example):**

``` text
Line 3: ERROR Database connection failed
Line 8: ERROR Request timed out
Total errors: 2
```

**Explanation:** Iterating over the file reads it one line at a time,
which is suitable for large log files. `rstrip()` removes the trailing
newline when printing.

## 20. Check whether a TCP port is open

``` python
import socket

host = "example.com"
port = 443

try:
    with socket.create_connection((host, port), timeout=3):
        print(f"Port {port} is open on {host}")
except (socket.timeout, OSError):
    print(f"Port {port} is not reachable on {host}")
```

**Output (example):**

``` text
Port 443 is open on example.com
```

**Explanation:** `socket.create_connection()` attempts a TCP connection.
A successful connection indicates that the port is reachable from the
machine running the script; it does not prove that the application is
healthy.

# 3. File handling and automation

## 21. Count the total number of lines in a file

``` python
filename = "app.log"
line_count = 0

with open(filename, "r", encoding="utf-8", errors="replace") as file:
    for _ in file:
        line_count += 1

print(f"Total lines: {line_count}")
```

**Output (example):**

``` text
Total lines: 1250
```

**Explanation:** Each iteration reads one line and increments the
counter. This approach avoids loading the entire file into memory.

## 22. Count ERROR occurrences in a file

``` python
filename = "app.log"
count = 0

with open(filename, "r", encoding="utf-8", errors="replace") as file:
    for line in file:
        count += line.count("ERROR")

print(f"Total ERROR occurrences: {count}")
```

**Output (example):**

``` text
Total ERROR occurrences: 12
```

**Explanation:** `str.count()` counts occurrences in each line. This
counts the literal, case-sensitive text `ERROR`, including multiple
occurrences on one line.

## 23. Find duplicate lines in a file

``` python
filename = "app.log"
seen = set()
duplicates = set()

with open(filename, "r", encoding="utf-8", errors="replace") as file:
    for line in file:
        line = line.rstrip("\n")

        if line in seen:
            duplicates.add(line)
        else:
            seen.add(line)

print("Duplicate lines:")
for line in sorted(duplicates):
    print(line)
```

**Output (example):**

``` text
Duplicate lines:
ERROR Connection timeout
INFO Service started
```

**Explanation:** `seen` tracks lines already read. Repeated lines are
added to `duplicates`. A set reports each duplicated line once.

## 24. Compare two files and display their differences

``` python
from pathlib import Path
import difflib

file1 = Path("old_config.txt")
file2 = Path("new_config.txt")

text1 = file1.read_text(encoding="utf-8").splitlines()
text2 = file2.read_text(encoding="utf-8").splitlines()

diff = difflib.unified_diff(
    text1,
    text2,
    fromfile=str(file1),
    tofile=str(file2),
    lineterm=""
)

print("\n".join(diff))
```

**Output (example):**

``` text
--- old_config.txt
+++ new_config.txt
@@ -1,2 +1,2 @@
 port=8080
-debug=false
+debug=true
```

**Explanation:** `unified_diff()` creates a readable line-by-line
difference. This example reads both files into memory, so for very large
files consider a streaming or external diff tool.

## 25. Read a CSV file using Python

``` python
import csv

with open("servers.csv", "r", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    for row in reader:
        print(row["hostname"], row["ip"])
```

**Input file (`servers.csv`):**

``` text
hostname,ip
web01,192.168.1.10
web02,192.168.1.11
```

**Output:**

``` text
web01 192.168.1.10
web02 192.168.1.11
```

**Explanation:** `csv.DictReader` reads each row as a dictionary, using
the header row as field names.

## 26. Read and update a JSON file

``` python
import json

filename = "config.json"

with open(filename, "r", encoding="utf-8") as file:
    config = json.load(file)

config["environment"] = "production"

with open(filename, "w", encoding="utf-8") as file:
    json.dump(config, file, indent=4)

print(config)
```

**Input file (`config.json`):**

``` json
{
    "application": "payments",
    "environment": "staging"
}
```

**Output:**

``` text
{'application': 'payments', 'environment': 'production'}
```

**Explanation:** `json.load()` parses JSON into Python objects.
`json.dump()` writes the updated dictionary back to the file. In
production, validate the data and use a safe write strategy if
interruption could corrupt an important configuration file.

## 27. Find the 10 largest files in a directory

``` python
import os
import heapq

directory = "/var/log"
file_sizes = []

for root, _, files in os.walk(directory):
    for filename in files:
        path = os.path.join(root, filename)

        try:
            size = os.path.getsize(path)
            file_sizes.append((size, path))
        except OSError:
            pass

for size, path in heapq.nlargest(10, file_sizes):
    print(f"{size / (1024 ** 2):.2f} MB  {path}")
```

**Output (example):**

``` text
250.40 MB  /var/log/app/archive.log
120.10 MB  /var/log/syslog
```

**Explanation:** `os.walk()` searches recursively, and
`heapq.nlargest()` returns the ten largest `(size, path)` pairs. The
displayed output may contain fewer than ten entries if fewer files
exist.

## 28. Search for a word in multiple files

``` python
from pathlib import Path

directory = Path("/var/log/myapp")
search_word = "ERROR"

for path in directory.glob("*.log"):
    try:
        with path.open("r", encoding="utf-8", errors="replace") as file:
            for line_number, line in enumerate(file, start=1):
                if search_word in line:
                    print(f"{path}:{line_number}: {line.rstrip()}")
    except OSError as error:
        print(f"Could not read {path}: {error}")
```

**Output (example):**

``` text
/var/log/myapp/app.log:12: ERROR Database unavailable
```

**Explanation:** `glob("*.log")` selects log files in the specified
directory. Each file is processed line by line, and matching lines are
printed with their line numbers.

## 29. Rename multiple files using Python

``` python
from pathlib import Path

directory = Path("/tmp/reports")

for old_path in directory.glob("*.txt"):
    new_path = old_path.with_name("archive_" + old_path.name)

    if new_path.exists():
        print(f"Skipping; destination exists: {new_path}")
        continue

    old_path.rename(new_path)
    print(f"Renamed {old_path.name} -> {new_path.name}")
```

**Output (example):**

``` text
Renamed report1.txt -> archive_report1.txt
Renamed report2.txt -> archive_report2.txt
```

**Explanation:** `Path.rename()` changes the filename. The
destination-exists check helps avoid unintentionally overwriting an
existing file.

## 30. Create a backup of a directory

``` python
from pathlib import Path
import shutil
from datetime import datetime

source = Path("/opt/myapp")
backup_root = Path("/opt/backups")

timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
backup_root.mkdir(parents=True, exist_ok=True)

archive_base = backup_root / f"myapp_{timestamp}"
archive_path = shutil.make_archive(
    str(archive_base),
    "gztar",
    root_dir=str(source.parent),
    base_dir=source.name
)

print(f"Backup created: {archive_path}")
```

**Output (example):**

``` text
Backup created: /opt/backups/myapp_20261119_103000.tar.gz
```

**Explanation:** `make_archive()` creates a compressed tar archive. The
timestamp gives each backup a distinct name. Ensure the process has read
permission on the source and write permission on the backup destination.

# 4. Regex and log parsing

## 31. Extract IPv4-shaped addresses from logs

``` python
import re

log = """
Connection from 192.168.1.10
Connection from 10.0.0.5
Connection from 172.16.0.1
"""

pattern = r"\b(?:\d{1,3}\.){3}\d{1,3}\b"
ips = re.findall(pattern, log)

print(ips)
```

**Output:**

``` text
['192.168.1.10', '10.0.0.5', '172.16.0.1']
```

**Explanation:** The pattern finds four groups of one to three digits
separated by dots. It finds IPv4-shaped strings but does not validate
that each octet is between `0` and `255`.

## 32. Extract email addresses using regex

``` python
import re

text = "Contact ops@example.com or admin@example.org"

pattern = r"\b[\w.+-]+@[\w.-]+\.[A-Za-z]{2,}\b"
emails = re.findall(pattern, text)

print(emails)
```

**Output:**

``` text
['ops@example.com', 'admin@example.org']
```

**Explanation:** The pattern matches common email-address formats. It is
useful for extraction but is not a complete standards-compliant email
validator.

## 33. Find HTTP 404 and 500 status codes

``` python
import re

log = """
GET /home 200
GET /login 404
POST /api 500
GET /dashboard 200
"""

errors = re.findall(r"\b(?:404|500)\b", log)

print(errors)
```

**Output:**

``` text
['404', '500']
```

**Explanation:** `(?:404|500)` matches either status code. Word
boundaries prevent matching those digits as part of a longer number.

## 34. Extract timestamps from logs

``` python
import re

log = """
2026-11-18 10:15:30 INFO Application started
2026-11-18 10:20:45 ERROR Database timeout
"""

pattern = r"\b\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\b"
timestamps = re.findall(pattern, log)

print(timestamps)
```

**Output:**

``` text
['2026-11-18 10:15:30', '2026-11-18 10:20:45']
```

**Explanation:** The pattern extracts timestamps in
`YYYY-MM-DD HH:MM:SS` format. It extracts the text shape and does not
validate calendar dates.

## 35. Find failed SSH login attempts and their IP addresses

``` python
import re

log = """
Failed password for root from 192.168.1.10 port 22 ssh2
Accepted password for ubuntu from 192.168.1.20 port 22 ssh2
Failed password for admin from 10.0.0.5 port 22 ssh2
"""

pattern = (
    r"Failed password for .*? from "
    r"((?:\d{1,3}\.){3}\d{1,3})"
)

failed_ips = re.findall(pattern, log)

print(failed_ips)
print(f"Failed attempts: {len(failed_ips)}")
```

**Output:**

``` text
['192.168.1.10', '10.0.0.5']
Failed attempts: 2
```

**Explanation:** The regex first finds lines containing the
failed-password message and captures the IP address after `from`. Real
SSH log formats vary, so adjust the pattern to match the target system's
logs.

## 36. Extract Docker container IDs

``` python
import re

text = """
Container ID: 0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef
"""

pattern = r"\b[0-9a-fA-F]{64}\b"
container_ids = re.findall(pattern, text)

print(container_ids)
```

**Output:**

``` text
['0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef']
```

**Explanation:** This pattern finds strings containing exactly 64
hexadecimal characters, a common full-length Docker container ID format.
Short IDs require a different pattern.

## 37. Find all ERROR and WARNING messages

``` python
import re

log = """
INFO Application started
ERROR Database unavailable
WARNING Disk usage high
INFO Health check passed
ERROR Request failed
"""

pattern = r"^.*\b(?:ERROR|WARNING)\b.*$"
matches = re.findall(pattern, log, flags=re.MULTILINE)

for line in matches:
    print(line)
```

**Output:**

``` text
ERROR Database unavailable
WARNING Disk usage high
ERROR Request failed
```

**Explanation:** `re.MULTILINE` makes `^` and `$` apply to individual
lines. The non-capturing group `(?:ERROR|WARNING)` matches either word.

## 38. Replace IP addresses in a log

``` python
import re

text = "Server IP is 192.168.1.10"

pattern = r"\b(?:\d{1,3}\.){3}\d{1,3}\b"
result = re.sub(pattern, "XXX.XXX.XXX.XXX", text)

print(result)
```

**Output:**

``` text
Server IP is XXX.XXX.XXX.XXX
```

**Explanation:** `re.sub()` replaces every match of the pattern with the
replacement text. As with question 31, this pattern matches IPv4-shaped
text rather than validating addresses.

# 5. Advanced DevOps automation

## 39. Connect to a remote Linux server using SSH

``` python
import paramiko

host = "192.0.2.10"
username = "devops"
key_path = "/home/devops/.ssh/id_ed25519"

client = paramiko.SSHClient()
client.load_system_host_keys()
client.set_missing_host_key_policy(paramiko.RejectPolicy())

try:
    client.connect(
        hostname=host,
        username=username,
        key_filename=key_path,
        timeout=10
    )

    stdin, stdout, stderr = client.exec_command("hostname")
    print(stdout.read().decode().strip())

finally:
    client.close()
```

**Output (example):**

``` text
web-server-01
```

**Explanation:** Paramiko provides SSH connectivity from Python. The
script uses a private key and checks the server host key against known
host keys. `RejectPolicy()` rejects unknown host keys rather than
trusting them automatically.

**Requirement:** Install with `python -m pip install paramiko`. Use a
real host, account, and key path that you are authorized to access.

## 40. Execute a command on multiple Linux servers using SSH

``` python
import paramiko

servers = ["192.0.2.10", "192.0.2.11"]
username = "devops"
key_path = "/home/devops/.ssh/id_ed25519"
command = "hostname"

for host in servers:
    client = paramiko.SSHClient()
    client.load_system_host_keys()
    client.set_missing_host_key_policy(paramiko.RejectPolicy())

    try:
        client.connect(
            hostname=host,
            username=username,
            key_filename=key_path,
            timeout=10
        )

        _, stdout, stderr = client.exec_command(command)
        exit_code = stdout.channel.recv_exit_status()

        print(f"\nServer: {host}")
        print(stdout.read().decode().strip())

        error_text = stderr.read().decode().strip()
        if error_text:
            print(f"Error: {error_text}")

        print(f"Exit code: {exit_code}")

    except Exception as error:
        print(f"Could not connect to {host}: {error}")

    finally:
        client.close()
```

**Output (example):**

``` text
Server: 192.0.2.10
web-server-01
Exit code: 0
```

**Explanation:** The script loops over a server list and executes the
same command on each host. It reports connection errors and command exit
codes. For large fleets, consider controlled concurrency, timeouts,
retries, and centralized logging.

## 41. Transfer a file using SFTP

``` python
import paramiko

host = "192.0.2.10"
username = "devops"
key_path = "/home/devops/.ssh/id_ed25519"

local_file = "/tmp/report.txt"
remote_file = "/tmp/report.txt"

client = paramiko.SSHClient()
client.load_system_host_keys()
client.set_missing_host_key_policy(paramiko.RejectPolicy())

try:
    client.connect(
        hostname=host,
        username=username,
        key_filename=key_path,
        timeout=10
    )

    sftp = client.open_sftp()
    try:
        sftp.put(local_file, remote_file)
        print("File uploaded successfully")
    finally:
        sftp.close()

finally:
    client.close()
```

**Output:**

``` text
File uploaded successfully
```

**Explanation:** `open_sftp()` creates an SFTP session over SSH, and
`put()` uploads a local file to the remote path. The destination
directory must exist and the account must have permission to write
there.

## 42. Restart a systemd service if it is stopped

``` python
import subprocess

service = "nginx"

check = subprocess.run(
    ["systemctl", "is-active", service],
    capture_output=True,
    text=True
)

if check.stdout.strip() != "active":
    print(f"{service} is not active; attempting restart")

    restart = subprocess.run(
        ["sudo", "systemctl", "restart", service],
        capture_output=True,
        text=True
    )

    if restart.returncode == 0:
        print(f"{service} restart command succeeded")
    else:
        print(f"Restart failed: {restart.stderr.strip()}")
else:
    print(f"{service} is running")
```

**Output (example):**

``` text
nginx is running
```

**Explanation:** The script checks service state and attempts a restart
only when the service is not active. The account must have appropriate
privileges, and production automation should also verify service health
after the restart.

## 43. Monitor CPU and memory and print alerts

``` python
import psutil
import time

while True:
    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory().percent

    print(f"CPU: {cpu}% | Memory: {memory}%")

    if cpu > 80:
        print("ALERT: CPU usage is above 80%")

    if memory > 80:
        print("ALERT: Memory usage is above 80%")

    time.sleep(4)
```

**Output (example):**

``` text
CPU: 85.0% | Memory: 72.0%
ALERT: CPU usage is above 80%
```

**Explanation:** The script samples CPU and memory utilization and
prints an alert when either exceeds its threshold. It runs continuously
until stopped with `Ctrl+C`.

**Requirement:** Install `psutil` using `python -m pip install psutil`.

## 44. Start or stop an AWS EC2 instance using Boto3

``` python
import boto3

region = "ap-south-1"
instance_id = "i-0123456789abcdef0"
action = "stop"  # Change to "start" when required.

ec2 = boto3.client("ec2", region_name=region)

if action == "start":
    response = ec2.start_instances(InstanceIds=[instance_id])
elif action == "stop":
    response = ec2.stop_instances(InstanceIds=[instance_id])
else:
    raise ValueError("Action must be 'start' or 'stop'")

print(response["StartingInstances"] if action == "start"
      else response["StoppingInstances"])
```

**Output (example):**

``` text
[{'InstanceId': 'i-0123456789abcdef0', 'CurrentState': {'Code': 64, 'Name': 'stopping'}, 'PreviousState': {'Code': 16, 'Name': 'running'}}]
```

**Explanation:** Boto3 calls the EC2 API to request a state change.
Replace the example instance ID and region with your own. The API
response indicates the requested transition; it does not mean the
instance has already finished starting or stopping.

**Requirement:** Install `boto3` and configure AWS credentials with
least-privilege permissions. Stopping an instance can affect workloads
and incur data or availability consequences.

## 45. List EC2 instances using Boto3

``` python
import boto3

ec2 = boto3.client("ec2", region_name="ap-south-1")
paginator = ec2.get_paginator("describe_instances")

for page in paginator.paginate():
    for reservation in page["Reservations"]:
        for instance in reservation["Instances"]:
            print(
                instance["InstanceId"],
                instance["State"]["Name"],
                instance.get("InstanceType", "unknown")
            )
```

**Output (example):**

``` text
i-0123456789abcdef0 running t3.micro
i-0123456789abcdef1 stopped t3.small
```

**Explanation:** `describe_instances` returns EC2 instance details. A
paginator handles responses that span multiple pages. The script prints
the instance ID, state, and type.

## 46. Upload a file to an S3 bucket using Boto3

``` python
import boto3

bucket_name = "my-company-backups"
local_file = "/tmp/report.txt"
object_key = "reports/report.txt"

s3 = boto3.client("s3")

s3.upload_file(local_file, bucket_name, object_key)

print(f"Uploaded {local_file} to s3://{bucket_name}/{object_key}")
```

**Output:**

``` text
Uploaded /tmp/report.txt to s3://my-company-backups/reports/report.txt
```

**Explanation:** `upload_file()` transfers a local file to an S3 object
key. The AWS identity needs permission to upload to the specified bucket
and key.

## 47. Check Docker container status using Python

``` python
import subprocess

result = subprocess.run(
    ["docker", "ps", "-a", "--format", "{{.Names}} {{.Status}}"],
    capture_output=True,
    text=True,
    check=True
)

for line in result.stdout.splitlines():
    print(line)
```

**Output (example):**

``` text
web-app Up 2 hours
redis Exited (0) 1 hour ago
```

**Explanation:** The Docker CLI lists all containers, including stopped
containers, because of `-a`. The Docker command must be installed, and
the user must have permission to access the Docker daemon.

## 48. List Kubernetes pods using the Python client

``` python
from kubernetes import client, config

# Uses the current kubeconfig context.
config.load_kube_config()

v1 = client.CoreV1Api()
pods = v1.list_pod_for_all_namespaces()

for pod in pods.items:
    print(
        pod.metadata.namespace,
        pod.metadata.name,
        pod.status.phase
    )
```

**Output (example):**

``` text
default nginx-7c5b6f7d8c-abcde Running
kube-system coredns-12345 Running
```

**Explanation:** The Kubernetes Python client loads the current
kubeconfig context and lists pods across namespaces. The configured
identity must have permission to list pods.

**Requirement:** Install with `python -m pip install kubernetes`. For
code running inside a pod, use `config.load_incluster_config()` instead
of `load_kube_config()`.

## 49. Check application health using an HTTP API

``` python
import requests

url = "https://example.com/health"

try:
    response = requests.get(url, timeout=5)

    if response.status_code == 200:
        print("Application is healthy")
    else:
        print(f"Application returned HTTP {response.status_code}")

except requests.exceptions.RequestException as error:
    print(f"Health check failed: {error}")
```

**Output (example):**

``` text
Application is healthy
```

**Explanation:** `requests.get()` sends an HTTP GET request. A timeout
prevents the script from waiting indefinitely. A `200` response is
treated as healthy here, but real health checks should follow the
application's documented health contract.

**Requirement:** Install with `python -m pip install requests`.

## 50. Trigger a Jenkins job using its REST API

``` python
import os
import requests
from requests.auth import HTTPBasicAuth

jenkins_url = "https://jenkins.example.com"
job_name = "deploy-app"
username = os.environ["JENKINS_USER"]
api_token = os.environ["JENKINS_API_TOKEN"]

url = f"{jenkins_url}/job/{job_name}/build"

response = requests.post(
    url,
    auth=HTTPBasicAuth(username, api_token),
    timeout=15
)

if response.status_code in (200, 201, 202):
    print("Jenkins build request submitted")
else:
    print(f"Build request failed: HTTP {response.status_code}")
    print(response.text)
```

**Output (example):**

``` text
Jenkins build request submitted
```

**Explanation:** The script sends a POST request to the Jenkins build
endpoint using a username and API token. Store credentials in
environment variables or a secrets manager, not directly in source code.
Some Jenkins configurations require a crumb for CSRF protection; use the
crumb issuer endpoint when required.

**Requirement:** Install `requests`, set `JENKINS_USER` and
`JENKINS_API_TOKEN`, and use a Jenkins account authorized to trigger the
job. The example assumes a job without parameters; parameterized jobs
use the `buildWithParameters` endpoint.

------------------------------------------------------------------------

# Quick revision

    No. Problem                            Key concept
  ----- ---------------------------------- -------------------------------------
      1 Reverse a string                   Slicing
      2 Find duplicate elements            Set and list
      3 Second-largest number              Comparison and tracking
      4 Palindrome                         Reverse and compare
      5 Character frequency                Dictionary
      6 Remove duplicates                  List membership
      7 Factorial                          Loop and multiplication
      8 Fibonacci series                   Multiple assignment
      9 Prime number                       Modulo and `for-else`
     10 Sort dictionary by values          `sorted()` and `lambda`
     11 Check server reachability          `subprocess` and ping
     12 CPU utilization                    `psutil`
     13 Memory utilization                 `psutil.virtual_memory()`
     14 Disk utilization                   `shutil.disk_usage()`
     15 Check process                      `psutil.process_iter()`
     16 Check service status               `systemctl` and `subprocess`
     17 Find files older than 7 days       `os.walk()` and timestamps
     18 Delete files older than 30 days    File deletion and safety
     19 Find ERROR messages                File iteration
     20 Check TCP port                     `socket`
     21 Count file lines                   File iteration
     22 Count ERROR occurrences            `str.count()`
     23 Find duplicate lines               Set
     24 Compare files                      `difflib`
     25 Read CSV                           `csv.DictReader`
     26 Read and update JSON               `json.load()` and `json.dump()`
     27 Find largest files                 `os.walk()` and `heapq`
     28 Search multiple files              `pathlib` and file iteration
     29 Rename files                       `pathlib.Path.rename()`
     30 Back up a directory                `shutil.make_archive()`
     31 Extract IP addresses               `re.findall()`
     32 Extract email addresses            Regex
     33 Find HTTP errors                   Regex alternation
     34 Extract timestamps                 Regex
     35 Find failed SSH logins             Regex capture groups
     36 Extract Docker IDs                 Regex and hexadecimal
     37 Find ERROR and WARNING lines       Regex and `MULTILINE`
     38 Replace IP addresses               `re.sub()`
     39 Connect using SSH                  Paramiko
     40 Run commands on multiple servers   Paramiko and loops
     41 Transfer files using SFTP          Paramiko SFTP
     42 Restart a stopped service          `systemctl` and `subprocess`
     43 Monitor CPU and memory             `psutil` and thresholds
     44 Start or stop EC2                  Boto3 EC2 client
     45 List EC2 instances                 Boto3 paginator
     46 Upload to S3                       Boto3 `upload_file()`
     47 Check Docker containers            Docker CLI and `subprocess`
     48 List Kubernetes pods               Kubernetes Python client
     49 Check application health           HTTP request and exception handling
     50 Trigger Jenkins job                REST API and authentication

------------------------------------------------------------------------

# Important Python modules for DevOps interviews

  Module / package      Common use
  --------------------- ------------------------------------------------
  `os`                  Files, directories, environment variables
  `sys`                 Command-line arguments and interpreter details
  `subprocess`          Execute Linux commands
  `re`                  Regex and log parsing
  `shutil`              File copying, archives, disk usage
  `pathlib`             Object-oriented file paths
  `time` / `datetime`   Timestamps and scheduling
  `json`                JSON configuration and API data
  `csv`                 CSV processing
  `logging`             Script and application logs
  `socket`              Network and port checks
  `psutil`              CPU, memory, disk, and process monitoring
  `requests`            REST API automation
  `paramiko`            SSH and SFTP
  `boto3`               AWS automation
  `kubernetes`          Kubernetes API automation

# Interview preparation tips

1.  Practise writing each script without copying it.
2.  Explain the purpose of every important function and library.
3.  Handle common exceptions such as `FileNotFoundError`,
    `PermissionError`, `OSError`, and network timeouts.
4.  For large files, process data line by line instead of loading
    everything into memory.
5.  Validate paths, hostnames, ports, and user input.
6.  Avoid hardcoding passwords, API tokens, and cloud credentials.
7.  Use least-privilege permissions for SSH, AWS, Docker, Kubernetes,
    and Jenkins.
8.  Test scripts in a non-production environment before automating
    changes or deletions.
9.  Be ready to explain how you would scale a script from one server to
    100 servers.
10. Know the difference between a script that submits an operation and
    one that verifies the operation completed successfully.

**Practice tip:** Start with questions 1--20, then practise file
handling and regex, and finally move to SSH, AWS, Docker, Kubernetes,
and Jenkins automation. Focus on understanding the logic rather than
memorizing the code.
