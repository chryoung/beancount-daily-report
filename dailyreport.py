import sys
import subprocess
import time
import os
from datetime import datetime
import dateutil.tz

def get_now():
    return datetime.now(dateutil.tz.gettz('Asia/Shanghai'))

def should_gen(output):
    now = get_now()
    today = str(now.date())
    return all([f.find(today) == -1 for f in os.listdir(output)]) # No today's report

def wait():
    time.sleep(300)

def generate_report(bc, report_type):
    result = subprocess.run(['bean-report', bc, report_type], capture_output=True)
    if result.returncode == 0:
        return result.stdout.decode('utf8')
    else:
        return 'Failed to generate report!'

def generate_report_file(bc, report_type, output):
    now = get_now()
    report_file = str(now.date()) + ' ' + report_type + '.txt'
    report = generate_report(bc, report_type)
    with open(os.path.join(output, report_file), 'w') as rf:
        rf.write(report)

bc_file = sys.argv[1]
output = sys.argv[2]
report_types = sys.argv[3:]
while True:
    if should_gen(output):
        for report_type in report_types:
            generate_report_file(bc_file, report_type, output)
    wait()
