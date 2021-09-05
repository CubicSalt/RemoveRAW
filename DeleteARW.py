import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-p', '--path', type = str, default = "./")
parser.add_argument('-a', '--arw_path', type = str, default = None)

args = parser.parse_args()

def DeleteARW(args):
    cnt = 0
    if not args.arw_path:
        args.arw_path = args.path
    for file in os.listdir(args.path):
        if file[-4:] == ".ARW":
            ARWFile = os.path.join(args.arw_path, file)
            JPGFile = os.path.join(args.path, file[:-3] + "JPG")
            # 如果不存在对应的 JPG 文件，则删除 ARW 文件
            if not os.path.isfile(JPGFile):
                print("Removing File: ", ARWFile)
                os.remove(ARWFile)
                cnt = cnt + 1
    print("File(s) Removed!")
    print("Total:", cnt, " File(s)")
        
if __name__ == "__main__":
    DeleteARW(args)