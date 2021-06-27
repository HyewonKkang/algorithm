# def solution(phone_book):
#     phone_book.sort()
#     for i in range(len(phone_book)-1):
#             if phone_book[i+1].startswith(phone_book[i]):
#                 return False
#     return True

def solution(phone_book):
    phone_book.sort()
    for num1, num2 in zip(phone_book, phone_book[1:]):
        if num2.startswith(num1):
            return False
    return True