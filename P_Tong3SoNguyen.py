numbers = input("Nhập 3 số nguyên cách nhau bởi dấu phẩy : ").split(',')
total = sum(int(num) for num in numbers)
print("Tổng ba số nguyên là : ", total)

