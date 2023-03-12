import re

str1 = "We are familiar with you."
str2 = "Well I know you very well."
#str1 = re.sub('[a-zA-Z]', ' ', str1)
#str2 = re.sub('[a-zA-Z]', ' ', str2)

D = []
for i in range(len(str1) + 1):
    row = []
    for j in range(len(str2) + 1):
        row.append(0)
    D.append(row)
    
    
for i in range(len(str1) + 1):
    D[i][0] = i

# Initialising first column:
for j in range(len(str2) + 1):
    D[0][j] = j

for i in range(1, len(str1) + 1):
    for j in range(1, len(str2) + 1):
        if str1[i - 1] == str2[j - 1]:
            D[i][j] = D[i - 1][j - 1]
        else:
            # Adding 1 to account for the cost of operation
            insertion = 1 + D[i][j - 1]
            deletion = 1 + D[i - 1][j]
            replacement = 1 + D[i - 1][j - 1]

            # Choosing the best option:
            D[i][j] = min(insertion, deletion, replacement)

print("Levenshtein Distance: ", D[len(str1)][len(str2)])
