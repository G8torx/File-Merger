
import shutil
from pathlib import Path

#Get the path of your first file
firstfile = Path(r"path here"Co)
#Get the path of your second file
secondfile = Path(r"path here")

newfile = input("Enter the name of the new file: ")
print()
print("The merged content of the 2 files will be in", newfile)

with open(newfile, "wb") as wfd:

	for f in [firstfile, secondfile]:
		with open(f, "rb") as fd:
			shutil.copyfileobj(fd, wfd, 1024 * 1024 * 10)

print("\nThe content is merged successfully.!")
