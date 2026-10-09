# -*- coding: utf-8 -*-
"""
Created on Fri Oct  9 22:58:16 2026

@author: anmoh
"""

import streamlit as st
import numpy as np
import plotly.graph_objects as go

def run_simulation(params, strategy="fixed"):
    rng = np.random.default_rng(params.get("seed", 42))
    duration = params["duration_min"]
    interval = params["fixed_interval"]
    rate = params.get("arrival_rate", 120)
    n_passengers = rng.poisson(rate * duration / 60)

    if strategy == "fixed":
        avg_wait = interval / 2 + 3
    else:
        avg_wait = interval / 2 * 0.6 + 2

    waits = rng.exponential(avg_wait, n_passengers)
    return {
        "strategy": strategy,
        "avg_wait": float(waits.mean()),
        "max_wait": float(waits.max()),
        "over_ratio": float((waits > 15).mean()),
        "served": int(n_passengers),
        "waits": waits.tolist(),
    }

st.title("🚌 调度运行演示")

if "params" not in st.session_state:
    st.warning("请先到「参数设置」页面配置参数。")
    st.stop()

params = st.session_state.params

col1, col2 = st.columns(2)
if col1.button("▶️ 运行固定调度"):
    st.session_state["res_fixed"] = run_simulation(params, "fixed")
if col2.button("▶️ 运行动态调度"):
    st.session_state["res_dynamic"] = run_simulation(params, "dynamic")

def show(res, color):
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("平均等待", f"{res['avg_wait']:.1f} min")
    c2.metric("最大等待", f"{res['max_wait']:.1f} min")
    c3.metric("超阈值比例", f"{res['over_ratio']*100:.1f}%")
    c4.metric("完成运输", res["served"])
    fig = go.Figure(go.Histogram(x=res["waits"], nbinsx=30, marker_color=color))
    fig.update_layout(title="等待时间分布", xaxis_title="等待（min）", height=350)
    st.plotly_chart(fig, use_container_width=True)

if "res_fixed" in st.session_state:
    st.subheader("固定调度结果")
    show(st.session_state["res_fixed"], "#5B8FF9")
if "res_dynamic" in st.session_state:
    st.subheader("动态调度结果")
    show(st.session_state["res_dynamic"], "#F6BD16")