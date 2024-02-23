import os
import logging
import os

current_file_path = os.path.abspath(__file__)
log_file_path = os.path.expanduser(f"{current_file_path}/cron.log")
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', filename=log_file_path)

def test_job():
    logging.info("Test job ran successfully")
    print("Test job ran successfully")