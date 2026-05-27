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

    #合并数据集和测试集的数据，ignore_index=True表示忽略原来的索引，重新从0开始分配索引
    df = pd.concat([train,test],ignore_index=True)
    #df会将缺失值转成nan
    #将title这一列全转换成字符串
    df["Title"] = df["Title"].astype(str)
    #将title这一列转换成的字符串去首尾空格
    df["Title"] = df["Title"].str.strip()
    #下面对描述列进行同样操作
    df["Description"] = df["Description"].astype(str)
    df["Description"] = df["Description"].str.strip()

    #检查有没有为空或是为nan的行
    check_empty_nan1 = df[["Title","Description"]].isin(["","nan"])
    #print(check_empty_nan1.sum())
    #这里可以检查到没有空行或者为nan的行数

    #需要指定doc_id以便于后续进行排序还能找到原本的行号
    df["doc_id"] = range(len(df))

    #不好看把doc_id这一列放在最前面
    #改列顺序，如果有其他没有提到的列会被丢掉
    df = df[["doc_id","Title","Description"]]

    print(df.head())

if __name__ == "__main__":
    docs = load_and_assign_docids()