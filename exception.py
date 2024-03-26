# #
# def test ():
#     try:
#         a = "testing"+ 1
#     except:
#         print("something went wrong")
# test()
a = input("Enter a number: ")
print(f'The multiplication table of {a} is:')
try:
    for i in range(1, 11):
        print(f'{int(a)} x {i} = {int(a)*i}')
except Exception as e:
    print("Inavalid Input")

try: 
    num = int(input("Enter a number :"))
except  ValueError :
    print("The input number is not an integer")



