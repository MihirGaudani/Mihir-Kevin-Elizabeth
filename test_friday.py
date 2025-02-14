import csv
import numpy as np

file = open("test.csv", "w", newline = None)

file_writer = csv.writer(file)

file_writer.wrightrow("Time", "Data")

for i in range(10):
    entry = np.random.random()
    now = time.time()
    file_writer.wrightrow([now, entry])

file.close()