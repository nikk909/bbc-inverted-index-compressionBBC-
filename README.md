# BBC News Inverted Index Compression / BBC 新闻倒排索引压缩实验

**EN:** Build a naive inverted index on the [Learn AI BBC](https://www.kaggle.com/competitions/learn-ai-bbc) news corpus, compress postings (gap + variable-byte / gamma) and dictionary (string + blocking + front coding), then evaluate size reduction and keyword search.

**中文：** 在 BBC 新闻数据集上构建未压缩倒排索引，对倒排记录表与词典进行压缩，对比体积并支持关键词检索。

## Setup / 环境

```bash
python -m venv venv
# Windows: .\venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

## Data / 数据

Download from Kaggle competition [learn-ai-bbc](https://www.kaggle.com/competitions/learn-ai-bbc/data) and place:

- `data/train.csv`
- `data/test.csv`

## Run / 运行

```bash
python main.py
```
