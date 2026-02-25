from random import *
# Character sets
digits = "1234567890"
punctuation = '!#$%&*+-=?@^_'
lowercase = 'qwertyuioplkmnjhbvgfcxdsza'
uppercase = 'QWERTYUIOPASDFGHJKLMNBVCXZ'

chars = ''

# Input prompts (in English)
cnt = int(input('Number of passwords to generate:'))
length = int(input('Lenght of each password:'))

isdig = input('Include digits? (y/n):')
islow = input('Include lowercase letters? (y/n):')
isupp = input('Include uppercase letters? (y/n):')
ispunc = input('Include symbols (!#$%&*+-=?@^_)? (y/n): ')
isstr = input('Include ambiguous characters (iloO0L1)? (y/n):')

# Build character pool
if isdig == "y":
    chars += digits
if islow == "y":
    chars += lowercase
if isupp == "y":
    chars += uppercase
if ispunc == "y":
    chars += punctuation
if isstr == "y":  # Exclude ambiguous if user says 'n'
    for c in 'iloO0L1':
      chars = chars.replace(c, '')

# Function to generate one password
def generate_password(char, lengh):
    if length > len(chars):
      print('Error: requested length exceed available characters!')
      return
    n = sample(char, lengh)
    print(''.join(n))  # No spaces - clean output

# Generate all passwords
for i in range(cnt):       
    generate_password(chars,length)