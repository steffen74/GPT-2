#!/usr/bin/env python

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
