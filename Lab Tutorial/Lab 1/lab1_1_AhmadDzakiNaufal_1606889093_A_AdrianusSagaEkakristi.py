def fungsi1(input_string):
    jawaban = str(input_string)*len(str(input_string))
    return jawaban
def fungsi2(input_string):
    jawaban = int(input_string)*len(str(input_string))
    return jawaban
input_string = input("masukan angka: ")
print (fungsi1(input_string))
print (fungsi2(input_string))
