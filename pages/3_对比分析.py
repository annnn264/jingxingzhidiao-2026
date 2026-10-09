# -*- coding: utf-8 -*-
"""
Created on Fri Oct  9 22:59:07 2026

@author: anmoh
"""

import streamlit as st
import plotly.graph_objects as go

st.title("📊 对比分析")

if "res_fixed" not in st.session_state or "res_dynamic" not in st.session_state:
    st.warning("请先在「调度运行演示」页面运行两种策略。")
    st.stop()

rf = st.session_state["res_fixed"]
rd = st.session_state["res_dynamic"]

metrics = ["平均等待", "最大等待", "超阈值比例"]
fixed_vals = [rf["avg_wait"], rf["max_wait"], rf["over_ratio"] * 100]
dyn_vals = [rd["avg_wait"], rd["max_wait"], rd["over_ratio"] * 100]

fig = go.Figure(data=[
    go.Bar(name="固定调度", x=metrics, y=fixed_vals, marker_color="#5B8FF9"),
    go.Bar(name="动态调度", x=metrics, y=dyn_vals, marker_color="#F6BD16"),
])
fig.update_layout(barmode="group", title="固定 vs 动态", height=400)
st.plotly_chart(fig, use_container_width=True)

st.markdown(f"""
### 改善幅度
- 平均等待：**{(rf['avg_wait']-rd['avg_wait'])/rf['avg_wait']*100:.1f}%**
- 最大等待：**{(rf['max_wait']-rd['max_wait'])/rf['max_wait']*100:.1f}%**
""")