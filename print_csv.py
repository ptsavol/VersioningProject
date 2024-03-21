fname = "data.csv"
with open(fname, "r") as f:
	print(f"Contents of {fname}")
	for line in	f.readlines():
		print(line)
