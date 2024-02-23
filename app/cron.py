import os
import logging

current_file_path = os.path.abspath(__file__)
log_path = '/'.join(current_file_path.split('/')[:-1])

log_file_path = os.path.expanduser(f"{log_path}/cron.log")
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', filename=log_file_path)

def test_job():
    logging.info("Test job ran successfully")
