import streamlit as st
import os
from markdown import markdown

# 定义 node 文件夹路径
node_folder = 'node'

# 显示页面标题
st.title('我的博客')

# 获取 node 文件夹中的所有 Markdown 文件
markdown_files = [f for f in os.listdir(node_folder) if f.endswith('.md')]

# 搜索框
search_term = st.sidebar.text_input('搜索笔记')

# 根据搜索框过滤文件列表
if search_term:
    filtered_files = [f for f in markdown_files if search_term.lower() in f.lower()]
else:
    filtered_files = markdown_files

# 文件列表框
selected_file = st.sidebar.radio('选择一个笔记', filtered_files)

# 读取并显示选中的 Markdown 文件内容
if selected_file:
    file_path = os.path.join(node_folder, selected_file)
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    html_content = markdown(content)
    st.markdown(f"## {selected_file}")
    st.markdown(html_content, unsafe_allow_html=True)
