scores = [ 23,24,25,26,27,28,29,39,31,32,33,34,35,36,37,38,38,39,62,23]

max_score = 0

for score in scores:
    if score > max_score:
        max_score = score

        print(max_score)

print(f"This is the max score: {max_score}")

#for loops with the range function
num = 0
for number in range(1, 101):
    print(number)
    num = num + number
    print(num)