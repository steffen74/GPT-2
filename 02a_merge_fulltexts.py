#!/usr/bin/env python

import re
import os

dir = "02_fulltexts-climate-change"
papers = []

with open("full_texts_merged.txt", "w") as out_file:
  for f_name in os.listdir(dir):
    path = os.path.join(dir, f_name)
    with open(path, "r") as f:
      f_text = ''.join(f.readlines()) # Fulltext as a single string
      f_text = re.sub(r"\n[^\n]", "", f_text) # Remove Carriage Return due to Scanning (i.e. only if no carriage return follows immediatly)
      #papers.append(f_text)
      out_file.write(f_text)
      out_file.write("\n")
