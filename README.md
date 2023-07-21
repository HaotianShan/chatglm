# 搭建本地知识库，基于开源大模型(LLM) chatglm-6B

## 简介
- 本文基于中文开源大模型 ChatGLM 构建本地知识库，用到了 chatglm-6b-int4 + text2vec-large-chinese 模型。
- KM文章：https://km.woa.com/vkm/articles/show/576792?ts=1683536354

## 安装部署
### 机器性能要求
默认参数在GTX1660Ti（6G显存）上运行良好。

### 自行安装
#### 1.安装库
通用依赖：```pip install -r requirements.txt```

#### 2.下载模型
根据需要，下载对应模型。
需下载模型[GanymedeNil/text2vec-large-chinese](https://huggingface.co/GanymedeNil/text2vec-large-chinese)置于model文件夹。

内部下载地址：
- https://drive.weixin.qq.com/s?k=AJEAIQdfAAoarZhuyh
- https://drive.weixin.qq.com/s?k=AJEAIQdfAAoHFpMDpO

解压缩模型文件
```
cd chatglm_knowledge/model
tar xf chatglm-6b-int4.tar.gz
tar xf text2vec-large-chinese.tar.gz
```

并将自己的txt格式语料置于txt文件夹。支持txt、pdf格式。
- 注意：txt文件夹里不能放不相关的文件，因为都会被读取

#### 3.参数设置
根据`config.xml`中说明，填写你的模型下载位置等信息

## 知识库
st模式，sentence_transformers+faiss进行索引

### st模式
sentence_transformers+faiss进行索引、匹配，并连同上下文返回，相当于原先x模式升级版。

#### 4.处理文本
构建索引执行```python plugins/gen_data_st.py```

#### 5.运行
执行```python main.py```
