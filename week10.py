import OS

directory = input('Enter the directory name:')
filename = directory+ input ('Enter the filename:')

name = input('Enter name:')
address = input('Enter Address:')
phone = input('Enter phone number:')

#creates directory
os.mkdir (directory)

#creates the file within the directory
with open("{}/{}.csv".format(directory, filename), 'w') as file:
    file.write(",".join([name, address, phone]) + "n")

# create file object to read from specified file in directory
with open("{}/{}.csv".format(directory, filename), 'r') as file:

  print("{}/{}.csv contents".format(directory, filename))

  # loop through each line in file and print to screen

  for line in file:

    print(line)
