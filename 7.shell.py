#ls ở đây dùng để liệt kê các tệp và thư mục 
#-l: tham số này yêu cầu lệnh ls hiển thị thông tin chi tiết về các tệp và thư mục ...
#-a thâm sô này yêu câu hiển thị tất cả các tệp, bao gồm tất cả các tệp ẩn(tệp có tên bắt đầu bằng dấu chấm)


import os
import subprocess as sp

# nhàm này cho phép người dùng thực hiện lệnh hệ thống bằng mô-đun os
def os_module():
    while True:
        cmd = input("$ ") # kí hiệu $ thường được sủ dụng trong tài liệu hướng dẫn biểu thị dấu nhắc lện trong terminal hay cmd
        # nhập lệnh từ người dùng 
        if cmd == "exit":
            break
        elif cmd == "pwd":
            print(os.getcwd())
        #getcwd là viết tắt của get current working directory     
        elif cmd.startswith("cd"):
            os.chdir(cmd[3:])
        # cắt chuỗi 

        else:
            os.system(cmd)


def subprocess_module():
    while True:
        cmd = input("$ ")
        if cmd == "exit":
            break
        elif cmd == "pwd":
            print(sp.run(["pwd"], capture_output=True).stdout.decode())
        elif cmd.startswith("cd"):
            sp.run(["cd", cmd[3:]])
        else:
            sp.run(cmd.split())


def main():
    choice = input("os or subprocess? ")
    match choice:
        case "os":
            os_module()
        case "subprocess":
            subprocess_module()
        case _:
            print("invalid choice")


if __name__ == "__main__":
    main()