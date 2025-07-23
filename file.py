# import csv

# input_files = ['file1.csv','file2.csv']
# output_file = 'file3.csv'

# with open (output_file,'w',newline='') as outfile:
#     writer = csv.writer(outfile)

#     header_written = False
#     for file in input_files:
#         with open(file,'r') as  f:
#             reader = csv.reader (f)
#             header = next(reader)

#             if not header_written:
#                 reader = csv.reader(header)
#                 header_written = True

#                 for row in reader:
#                     writer.writerow(row)

#                     print("files merged successfully into 'mergedfile.csv'")