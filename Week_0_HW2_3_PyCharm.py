# week 0 - hw 2.3 - PyCharm
# Problem:
# Write a Python program to accept a filename from the user and print the extension of that.
# Sample filename : abc.java
# Output : java

# Solution

print('Please insert a filename with its extension:')
file_name_with_ext = input()
len_file_name = len(file_name_with_ext)
pos = file_name_with_ext.rfind('.')
print("extension of the file is:", file_name_with_ext[pos + 1:len_file_name])
