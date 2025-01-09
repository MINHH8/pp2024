import os
from zipfile import ZipFile

# Đường dẫn đến thư mục chứa các file .txt
directory = 'D:\minh\python\student.dat'  # Thay đổi đường dẫn này theo thư mục của bạn
zip_filename = 'student.date.zip'  # Tên file zip sẽ được tạo

# Tạo file zip
with ZipFile(zip_filename, 'w') as zip_file:
    # Duyệt qua tất cả các file trong thư mục
    for filename in os.listdir(directory):
        if filename.endswith('.txt'):  # Kiểm tra xem file có là .txt không
            # Tạo đường dẫn đầy đủ cho file
            file_path = os.path.join(directory, filename)
            # Thêm file vào zip
            zip_file.write(file_path, arcname=filename)

print(f"Đã nén các file .txt thành {zip_filename}.")