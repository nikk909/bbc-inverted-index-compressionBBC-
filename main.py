import pandas as pd
from pathlib import Path

data_dir = Path("data")
train_path = data_dir/"train.csv"
test_path = data_dir/"test.csv"

def load_and_assign_docids() ->pd.DataFrame:#return type hint返回类型标注
    
    #只读取标题和描述列，不读取第一列的分类id
    cols = ["Title","Description"]
    train = pd.read_csv(train_path,usecols=cols)
    test = pd.read_csv(test_path,usecols=cols)

    df = pd.concat([train,test],ignore_index=True)
    #df会将缺失值转成nan
    #将title这一列全转换成字符串
    df["Title"] = df["Title"].astype(str)
    #将title这一列转换成的字符串去首尾空格
    df["Title"] = df["Title"].str.strip()
    #下面对描述列进行同样操作
    df["Description"] = df["Description"].astype(str)
    df["Description"] = df["Description"].str.strip()

    #展示
    for i in range(5):
        #默认先列后行。也可以是df.loc[i,"Title"]
        print(f"Title: {df['Title'][i]}")
        print("--------------------------------")
        print(f"Description: {df['Description'][i]}")
        print("--------------------------------")

    return df

if __name__ == "__main__":
    docs = load_and_assign_docids()