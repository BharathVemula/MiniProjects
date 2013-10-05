import os
file_size = os.stat(sys.argv[1]).st_size
print file_size
