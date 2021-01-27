## The following script contains three different code-blocks for paper-preparation:

## The first approach the papers in the climate-change folder are simply pasted together

import os
dir = 'drive/MyDrive/NLP_scientific-text-generation/02_fulltexts-climate-change'

with open ("fulltexts.txt", "w") as out_file:
  for f_name in os.listdir(dir):
    path = os.path.join(dir, f_name)
    with open(path, 'r') as f:
      f_text = ''.join(f.readlines())
      f_text += "\n"
    out_file.write("%s\n" % f_text)
    
    
## In the second approach the papers will be written in a single line each. 

import re

dir = 'drive/MyDrive/NLP_scientific-text-generation/02_fulltexts-climate-change'
papers = []

for f_name in os.listdir(dir):
  path = os.path.join(dir, f_name)
  with open(path, "r") as f:
    f_text = ''.join(f.readlines()) # Fulltext as a single string
    f_text = re.sub(r"\n[^\n]", "", f_text) # Remove Carriage Return due to Scanning (i.e. only if no carriage return follows immediatly)
    papers.append(f_text)

with open('fulltext_papers_linewise.txt', 'w') as f:
    for item in papers:
        f.write("%s\n" % item)
        

## In the third approach carriage returns as well as short lines are removed, in order to get rid of tables etc...
        
import re
import os

dir = "02_fulltexts-climate-change"

with open("full_texts_merged.txt", "w") as out_file:
  for f_name in os.listdir(dir):
    path = os.path.join(dir, f_name)
    with open(path, "r") as f:
      lines = []
      for line in f:
        if len(line) > 20 or line == "\n": # Remove short lines that are likely result of tables
          lines.append(line)
      f_text = "".join(lines) # Fulltext as a single string
      # Remove Carriage Return due to Scanning (i.e. only if no carriage return follows immediatly)
      f_text = re.sub(r"\n(?!\n)", " ", f_text)
      # Strip leading whitespaces left over from previous step, remove empty lines
      f_text = re.sub(r"(\s?\n\s?)+", "\n", f_text)
      # Strip lines shorter than 50 chars, only leaving full paragraphs of text
      f_text = re.sub(r"\n(.{0,50})(?=\n)", "", f_text)
      # Remove leading and trailing whitespace
      f_text = f_text.strip()
      out_file.write(f_text)