with open("data2.txt", "r", encoding="utf-8") as i:
  with open("data3.txt", "w", encoding="utf-8") as o:
    
    buffer = ""
    for line in i:
      if line.startswith("–"):
        if buffer:
          o.write(buffer + "\n")
        buffer = line.strip()
      else:
        buffer += line.strip()
    if buffer:
      o.write(buffer)