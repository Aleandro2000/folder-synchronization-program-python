Folder Synchronization Program

Description:
--------------
This Python script is used to synchronize two folders: source and replica. It maintains a one-way synchronization, ensuring that the content of the replica folder matches the content of the source folder.

Usage:
--------------
To use this program, follow these steps:

1. Install the required packages using pip:

pip install -r requirements.txt


2. Run the script with the following command:

python main.py source_folder replica_folder sync_log.txt


Replace "source_folder" with the path to the source folder, "replica_folder" with the path to the replica folder, and "sync_log.txt" with the desired log file path.

3. The script will periodically synchronize the folders, log file operations, and display output on the console.

Dependencies (requirements.txt):
--------------
- os-sys (or os, if you meant the built-in os module)
- shutil
- filecmp
- argparse
- logging
- schedule
- time

Author:
--------------
Alexandru-Andrei Carmici