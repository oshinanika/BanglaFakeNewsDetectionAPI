import logging
from mlapp import app
from datetime import date
from pathlib import Path

'''
Developed By: Md. Imtiyaz Hossain 
Designation: Software Engineer
Team: Mobile App
Development Start: 20 Mar, 2020
Latest Update: 9 June, 2020
'''
root_log_path = app.config.get("LOG_PATH")

def error_logs(error):
     log_filename = '{}/error_logs_{}.log'.format(root_log_path, date.today())
     logging.basicConfig(filename=Path(log_filename), level=logging.ERROR,
                        format='%(asctime)s %(levelname)s %(name)s %(message)s')
     logger = logging.getLogger(__name__)
     logger.error(error)


