# Beancount Daily Report

Build daily report for the beancount file

## Build

`docker build -t beancount-daily-report .`

## Run

`docker run -d -e REPORT_TYPES="cash trial networth" -e BEANCOUNT_FILE="journal_file_name.beancount" -v folder/path/to/journal:/beancount -v folder/path/to/report/output:/reports beancount-daily-report`
