import os
import re


# for root, dirs, files in os.walk('C:\\Users\\patry\\Desktop\\STUDIA'):
#     for filenames in files:
#         if 'git' not in root and 'idea' not in root:
#             print(root, filenames)

# for root, dirs, files in os.walk('C:\\Users\\patry\\Desktop\\STUDIA'):
#     for filenames in files:
#         if '.' not in root:
#             print(root, filenames)

for root, dirs, files in os.walk('C:\\Users\\patry\\Desktop\\STUDIA'):
    for filenames in files:
        x = re.search('[\.]', root)
        y = re.search('\.idea', root)
        
        if x is None and y is None:
            print(root, filenames)
            
            


