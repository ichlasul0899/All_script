#!/usr/bin/env python3

import re
import csv

user_dict={}
error_dict={}

with open("syslog.log") as file:
        error_pattern = r"ERROR ([\w\s\']+) \(([\w\.]+)\)"
        info_pattern = r"INFO ([\w\s\'\[\]\#]+) \(([\w\.]+)\)"
        for line in file.readlines():
                result = re.search(error_pattern, line)
                result2 = re.search(info_pattern, line)
                print(result,result2)
                if result:
                        error_dict[result.group(1)] = error_dict.get(result.group(1), 0) + 1
                        user_dict[result.group(2)] = tuple(map(sum, zip(user_dict.get(result.group(2), (0, 0)), (0,1))))
                if result2:
                        #print(result.groups())
                        user_dict[result2.group(2)] = tuple(map(sum, zip(user_dict.get(result2.group(2), (0, 0)), (1,0))))
#print(user_dict,"\n\n", error_dict)
errors = sorted(error_dict.items(), key=lambda x:x[1], reverse=True)
users = sorted(user_dict.items())
print(errors,"\n", users)
error_fields = ["Error", "Count"]
user_fields = ["Username", "INFO", "ERROR"]
with open("error_message.csv", "w") as f:
        writer = csv.writer(f)
        writer.writerow(error_fields)
        for row in errors:
                writer.writerow(row)

with open("user_statistics.csv", "w") as f2:
        writer = csv.writer(f2)
        writer.writerow(user_fields)
        for row in users:
                row = [row[0],row[1][0],row[1][1]]
                writer.writerow(row)
