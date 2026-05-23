from pathlib import Path
import pandas as pd

DATA_DIR = Path("data")
TRAIN_PATH = DATA_DIR / "train.csv"
TEST_PATH = DATA_DIR / "test.csv"


def load_and_assign_docids() -> pd.DataFrame:
    """阶段一：合并 train/test，去空行，分配 DocID。"""
    train = pd.read_csv(TRAIN_PATH)
    test = pd.read_csv(TEST_PATH)

    # 标记来源（可选，方便以后分析）
    train["split"] = "train"
    test["split"] = "test"

    # 1) 混合训练集和测试集
    df = pd.concat([train, test], ignore_index=True)

    # 2) 清洗空行：标题和正文都空 / 全是空白
    df["Title"] = df["Title"].astype(str).str.strip()
    df["Description"] = df["Description"].astype(str).str.strip()

    before = len(df)
    df = df[
        ~((df["Title"] == "") & (df["Description"] == ""))
        & ~(df["Title"].eq("nan") & df["Description"].eq("nan"))
    ].copy()
    after = len(df)
    print(f"去掉空行: {before - after} 条，剩余 {after} 条")

    # 3) DocID：从 0 连续编号
    df["doc_id"] = range(len(df))

    assert df["doc_id"].is_unique
    assert df["doc_id"].min() == 0
    assert df["doc_id"].max() == len(df) - 1

    print(f"DocID 范围: 0 ~ {df['doc_id'].max()}，共 {len(df)} 篇")
    return df


if __name__ == "__main__":
    docs = load_and_assign_docids()
    print(docs[["doc_id", "Title"]].head())