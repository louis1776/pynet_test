with open ("myfile_w.txt", "w") as f:
    f.write("You got it!")
    f.close()

with open ("myfile_w.txt", "a") as f:
    f.write("\nAppended this line!")
    f.close()
