#!/usr/bin/env python

import re
import os

dir = "02_fultexts-climate-change"
papers = []

with open("full_texts_merged.txt", "w") as out_file:
  for f_name in os.listdir(dir):
    path = os.path.join(dir, f_name)
    with open(path, "r") as f:
      lines = []
      for line in f:
        if len(line) > 20: # Remove short lines that are likely result of tables
          lines.append(line)
      f_text = "".join(lines) # Fulltext as a single string
      f_text = re.sub(r"\n(?!\n)", " ", f_text) # Remove Carriage Return due to Scanning (i.e. only if no carriage return follows immediatly)
      f_text = re.sub(r"\n+(?=\n)", "", f_text) # Remove empty lines
      #papers.append(f_text)
      out_file.write(f_text)
      out_file.write("\n")
