file = open("output_mapped_reads2", "r")
file2 = open("output_result2", "a")
for line in file:
    if "exactly" in line:
        print line
        file2.write(line)
file2.close()
file.close()