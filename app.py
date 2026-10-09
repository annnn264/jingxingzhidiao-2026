# -*- coding: utf-8 -*-
"""
Created on Fri Oct  9 22:16:38 2026

@author: anmoh
"""

import streamlit as st

st.set_page_config(
    page_title="景行智调",
    page_icon="🚌",
    layout="wide",
)

st.title("🚌 景行智调")
st.subheader("景区接驳运力动态调度与可视化仿真系统")

st.markdown("""
### 项目简介
面向景区节假日高峰客流的接驳运力协同优化系统。
以南京钟山风景区为案例，通过仿真对比固定调度与动态调度。

👉 请从左侧导航进入各功能页面。
""")

st.info("⚠️ 本系统为仿真原型，结果由程序生成，不代表景区实测结果。")