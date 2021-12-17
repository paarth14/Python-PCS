# Write a Program that generates the multiplication table from 2 to 20 and write it to different files. Place these files in the 'tables' folder.

for i in range(2,21):
    with open(f"tables/Multiplication_table_of_{i}.txt", 'w') as f:
        for j in range(1,11):
            f.write(f"{i} x {j} = {i*j}")
            if j!=10:
                f.write("\n")
