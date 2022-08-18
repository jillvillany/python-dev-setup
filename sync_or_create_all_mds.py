import os
import re

directory = "./code_examples/"

"""
Handle Conversion of PY, HTML, JS, JSON, SH, Dockerfile and SQL files
"""
file_list = list()

# list of .py files not to convert to a markdown file
py_exclusion_patterns = list()
py_exclusion_patterns.append(".*webscraping-scrapy_spider/pop_quotes/[^/]*py")
py_exclusion_patterns.append(".*webscraping-scrapy_spider/pop_quotes/spiders/__init__.py")
py_exclusion_patterns.append(".*4-model_validation/pytest_testing/feature_extractors/.*\.py")
py_exclusion_patterns.append(".*4-model_validation/pytest_testing/utils/.*\.py")
py_exclusion_patterns.append(".*4-model_validation/pytest_testing/hybrid_medical_classifier.py")

for root, subdirectories, files in os.walk(directory):
    for file in files:
        if file.endswith('.py'): 
            fp = os.path.join(root, file)
            # check that it's not a python file we want to exclude
            # i.e. the init/ component files of modules like scrapy
            create_md = True
            for pattern in py_exclusion_patterns:
                if re.search(pattern, fp):
                    create_md = False
            if create_md:
                file_list.append(fp)
        elif file.endswith('.sh'):
            fp = os.path.join(root, file)
            file_list.append(fp)
        elif file.startswith('Dockerfile') and not file.endswith('.md'):
            fp = os.path.join(root, file)
            file_list.append(fp)
        elif file.endswith('.sql'):
            fp = os.path.join(root, file)
            file_list.append(fp)

# Add the html, js and json files you want included
# html
file_list.append('code_examples/5-deployment_and_full_stack/model_API_UI/main.html')
file_list.append('code_examples/6-data_visualization/amcharts/main.html')
# js
file_list.append('code_examples/6-data_visualization/tensorflow-js_model_development_dashboard/script.js')


i = 1
file_count = len(file_list)
for i,file in enumerate(file_list):
    with open(file) as f:
        text = f.read()
    f.close()

    fname = file.split('/')[-1]

    if file.endswith('.py'):
        md = "```python\n" + text + "\n```"
        md_fn = file.replace(".py", ".md")
    elif file.endswith('.html'):
        md = "```html\n" + text + "\n```"
        md_fn = file.replace(".html", ".md")
    elif file.endswith('.js'):
        md = "```js\n" + text + "\n```"
        md_fn = file.replace(".js", ".md")
    elif file.endswith('.css'):
        md = "```css\n" + text + "\n```"
        md_fn = file.replace(".css", ".md")
    elif file.endswith('.sh'):
        md = "```bash\n" + text + "\n```"
        md_fn = file.replace(".sh", ".md")
    elif fname.startswith('Dockerfile') and not fname.endswith('.md'):
        md = "```Dockerfile\n" + text + "\n```"
        md_fn = file.replace("Dockerfile.", "Dockerfile_") + ".md"
    elif file.endswith('.sql'):
        md = "```sql\n" + text + "\n```"
        md_fn = file.replace(".sql", ".md")
    elif file.endswith('.json'):
        md = "```json\n" + text + "\n```"
        md_fn = file.replace(".json", ".md")
    
    with open(md_fn, "w") as f:
        f.write(md)
    f.close()

    print('{} of {} wrote {}'.format(i, file_count,md_fn))
    i+=1


"""
Handle Conversions for IPYNB Files
"""

ipynb_files = list()

for root, subdirectories, files in os.walk(directory):
    for file in files:
        if file.endswith('.ipynb') and '.ipynb_checkpoints/' not in file:
            ipynb_files.append(os.path.join(root, file))

ipynb_files_count = len(ipynb_files)
i = 1
print('Creating .md verion of .ipynb files...')
for file in ipynb_files:
    # print(file)
    cmd = 'jupyter nbconvert --to markdown {}'.format(file)
    print('{} of {} {}'.format(i,ipynb_files_count,cmd))
    stream = os.popen(cmd)
    output = stream.read()
    i += 1

    file_md = file.replace(".ipynb", ".md")
    with open(file_md, "r") as f:
        text = f.read()
        """
        NOTE: adding ```<div class = "df-div">``` around table elements so we can include table scrolling in the custom css defined in "code_examples/css/custom_style.css" with the following code:
        ```css
        .df-div {
        overflow-x:auto;
        }
        """
        text = text.replace('<div>\n<style scoped>', '<div class = "df-div">\n<style scoped>')
    f.close()

    print("Updating markdown format of ",file_md)
    with open(file_md, "w+") as f:
        f.write(text)
    f.close()
