# alphabet files
digit_file = "bin_digits.txt"
alphabet_file = "alphabet.txt"
# temp arrs
bin_numbers_arr = []
letter_arr = []
# dictionary for letter-to-bin coding
letter_to_bin = {}
# dictionary for bin-to-letter coding
bin_to_letter = {}
# amount of letters
alphabet_amount = 41

# creating the arrs
f = open(digit_file, 'r')
for line in f:
    bin_numbers_arr.append(line.replace("\n", ""))
f.close()

f = open(alphabet_file, 'r')
for letter in range(41):
    letter_arr.append(f.read(1))
f.close()

# checking the arrs
print(letter_arr)
print(bin_numbers_arr)

# dict creating
for i in range(alphabet_amount):
    letter_to_bin[letter_arr[i]] = bin_numbers_arr[i]

for i in range(alphabet_amount):
    bin_to_letter[bin_numbers_arr[i]] = letter_arr[i]

# checking the dicts
print(letter_to_bin)
print(bin_to_letter)


key = int(input(" Input 1 to code, 2 to decode "))

# Coding
if key == 1:

    text_to_code = str(input("введите русский текст маленькими буквами "))
    answer = ''

    for letter in text_to_code:
        answer = answer + letter_to_bin[letter]

    print(answer)
else:
    # Decoding

    decoded_answer = ''
    dig_group = ""
    dig_group_length = 6
    amount_counter = 0
    text_to_decode = str(input("ведите последовательность из 0 и  1 "))

    for number in text_to_decode:
        dig_group = dig_group + number
        amount_counter += 1
        if amount_counter >= dig_group_length:
            amount_counter = 0
            decoded_answer = decoded_answer + bin_to_letter[dig_group]
            dig_group = ''

    print(decoded_answer)


