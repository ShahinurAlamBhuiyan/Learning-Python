from pathlib import Path

# Absolute path  --> path start from root of our disk
# Relative path  --> path starting from current path

path = Path("ecommerce")
# print(path.exists())
# path.mkdir()  # creating directory. return None
# print(path.exists())

# path.rmdir()  # remove directory return None
# print(path.exists())

path1 = Path()
# (path1.glob('*.*'))  # *.* only get the files. *.py getting all py files
for file in path1.glob('*'):
    print(file)




