# Description for glue_data
## MRPC
MRPC(The Microsoft Research Paraphrase Corpus，微软研究院释义语料库)，相似性和释义任务，是从在线新闻源中自动抽取句子对语料库，并人工注释句子对中的句子是否在语义上等效。
类别并不平衡，其中68%的正样本，所以遵循常规的做法，报告准确率（accuracy）和F1值。
### 任务
是否释义二分类，是释义，不是释义两类。
### 评价准则
准确率（accuracy）和F1值。
### tsv文件解释
tab分割的文件，每行有4个用Tab分割的字符
index,id1,id2,string1,string2
1	
702876  
702977	
Amrozi accused his brother, whom he called "the witness", of deliberately distorting his evidence.	
Referring to him as only "the witness", Amrozi accused his brother of deliberately distorting his evidence.

> 输入两个句子，模型判断它们是否同一个意思。
* train.tsv:第一列0或1，0代表不同意思，1代表同意思。
* test.tsv:第一列就是index，无意义