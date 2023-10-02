#Author: Alexandru-Andrei Carmici

import os
import shutil
import filecmp
import argparse
import logging
import schedule
import time

def synchronize_folders(source_path, replica_path, log_path):
    logging.basicConfig(filename=log_path, level=logging.INFO, format='%(asctime)s - %(message)s')
    console_logger = logging.StreamHandler()
    console_logger.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s - %(message)s')
    console_logger.setFormatter(formatter)
    logger = logging.getLogger()
    logger.addHandler(console_logger)

    def copy_or_delete(src, dst, operation):
        if operation == 'copy':
            shutil.copy(src, dst)
            logger.info(f'Copied {src} to {dst}')
        elif operation == 'delete':
            os.remove(dst)
            logger.info(f'Deleted {dst}')

    comparison = filecmp.dircmp(source_path, replica_path)
    for src_file in comparison.left_only:
        src_file_path = os.path.join(source_path, src_file)
        replica_file_path = os.path.join(replica_path, src_file)
        copy_or_delete(src_file_path, replica_file_path, 'copy')

    for del_file in comparison.right_only:
        replica_file_path = os.path.join(replica_path, del_file)
        copy_or_delete(None, replica_file_path, 'delete')

    schedule.every(1).hours.do(synchronize_folders, source_path, replica_path, log_path)

def main():
    parser = argparse.ArgumentParser(description='Folder Synchronization Program')
    parser.add_argument('source', help='Source folder path')
    parser.add_argument('replica', help='Replica folder path')
    parser.add_argument('log', help='Log file path')
    args = parser.parse_args()

    synchronize_folders(args.source, args.replica, args.log)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == '__main__':
    main()
