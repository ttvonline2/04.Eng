import random

# Đọc dữ liệu từ file data.txt vào một danh sách
with open("data.txt", "r") as file:
    lines = file.readlines()

# Loại bỏ khoảng trắng và ký tự xuống dòng từ các dòng
lines = [line.strip() for line in lines]

while lines:
    # Chọn một dòng ngẫu nhiên từ danh sách
    random_line = random.choice(lines)
    
    # In dòng được chọn ra màn hình
    print(random_line)
    
    # Yêu cầu người dùng nhập
    user_input = input("Nhập 'Y' để giảm giá trị, 'N' để tăng giá trị, hoặc 'E' để lưu và thoát: ").strip().lower()
    
    if user_input == 'y':
        # Tách từ và số từ dòng
        parts = random_line.split(", ")
        word = parts[0]
        value = int(parts[1])
        
        # Giảm giá trị đi 1 đơn vị
        value -= 1
        
        # Cập nhật lại dòng
        new_line = f"{word}, {value}\n"
        
        # Xoá dòng nếu giá trị là 0
        if value == 0:
            lines.remove(random_line)
        else:
            # Cập nhật dòng trong danh sách
            lines[lines.index(random_line)] = new_line
    
    elif user_input == 'n':
        # Tách từ và số từ dòng
        parts = random_line.split(", ")
        word = parts[0]
        value = int(parts[1])
        
        # Tăng giá trị lên 3 đơn vị
        value += 3
        
        # Cập nhật lại dòng
        new_line = f"{word}, {value}\n"
        
        # Cập nhật dòng trong danh sách
        lines[lines.index(random_line)] = new_line
    
    elif user_input == 'e':
        # Lưu tất cả thay đổi vào file data.txt
        with open("data.txt", "w") as file:
            file.writelines(lines)
        
        print("Dữ liệu đã được cập nhật và lưu vào file data.txt.")
        break  # Kết thúc chương trình

# Khi danh sách rỗng hoặc người dùng nhập 'E', thoát khỏi vòng lặp
print("Danh sách đã hết hoặc bạn đã lựa chọn lưu và thoát!")
