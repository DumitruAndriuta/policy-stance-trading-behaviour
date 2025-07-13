# Open the input file
with open("output.txt", "r") as file:
    lines = file.readlines()

# Round up each number and store them in a list
rounded_numbers = []
for line in lines:
    numbers = line.split()
    rounded_line = " ".join([str(round(float(num_str), 3)) for num_str in numbers])
    rounded_numbers.append(rounded_line)

# Write the rounded numbers back to the file
with open("rounded_output.txt", "w") as file:
    file.write("\n".join(rounded_numbers))