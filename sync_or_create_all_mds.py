import os
import re

directory = "docs/"

"""
Handle Conversion of SH files
"""
file_list = list()

for root, subdirectories, files in os.walk(directory):
    for file in files:
        if file.endswith('.sh'):
            fp = os.path.join(root, file)
            file_list.append(fp)

i = 1
file_count = len(file_list)
for i,file in enumerate(file_list):
    with open(file) as f:
        text = f.read()
    f.close()

    fname = file.split('/')[-1]

    if file.endswith('.sh'):
        md = "```bash\n" + text + "\n```"
        md_fn = file.replace(".sh", ".md")
    
    with open(md_fn, "w") as f:
        f.write(md)
    f.close()

    print('{} of {} wrote {}'.format(i, file_count,md_fn))
    i+=1
