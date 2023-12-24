import os
import pandas as pd

def process_csv(directory):
    # 遍历指定目录下的所有文件
    for filename in os.listdir(directory):
        if filename.endswith(".csv"):
            file_path = os.path.join(directory, filename)
            
            # 使用pandas读取csv文件
            df = pd.read_csv(file_path)
            
            # 删除包含缺失值的行
            df = df.dropna()
            
            # 保存到原文件
            df.to_csv(file_path, index=False)
            print(f"Processed {file_path}")

if __name__ == "__main__":
    directory = '/home/ubuntu/proj/rt-dataset/src/data'
    process_csv(directory)
