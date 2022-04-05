import multiprocessing, os

bind = '0.0.0.0:8000'
# workers = multiprocessing.cpu_count() * 2 + 1
workers = 1
timeout = 120
loglevel = "info"
