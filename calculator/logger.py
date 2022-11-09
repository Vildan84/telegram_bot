from datetime import datetime
import csv


# def log(msg, answer):
#     dic = {"Date": None, "Input": None, "Output": None}
#     time = datetime.now()
#     dic["Date"] = time
#     dic["Input"] = msg
#     dic["Output"] = answer
#     with open("files/logger.csv", "a", newline="") as csvfile:
#         fieldnames = ["Date", "Input", "Output"]
#         writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
#         writer.writeheader()
#         writer.writerow(dic)
