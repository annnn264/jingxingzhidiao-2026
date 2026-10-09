# -*- coding: utf-8 -*-
"""
Created on Fri Oct  9 22:54:35 2026

@author: anmoh
"""

import streamlit as st

st.title("⚙️ 仿真参数设置")
st.caption("所有参数均为仿真设定（D类），不代表景区实测值。")

if "params" not in st.session_state:
    st.session_state.params = {
        "duration_min": 480,
        "vehicle_count": 5,
        "vehicle_capacity": 30,
        "driver_count": 4,
        "fixed_interval": 15,
        "arrival_rate": 120,
        "seed": 42,
    }

p = st.session_state.params

p["duration_min"] = st.number_input("仿真时长（分钟）", 60, 1440, p["duration_min"], 30)
p["vehicle_count"] = st.slider("车辆总数", 1, 20, p["vehicle_count"])
p["vehicle_capacity"] = st.slider("车辆容量", 10, 60, p["vehicle_capacity"])
p["driver_count"] = st.slider("驾驶员总数", 1, 20, p["driver_count"])
p["fixed_interval"] = st.slider("固定发车间隔（分钟）", 5, 60, p["fixed_interval"])
p["arrival_rate"] = st.slider("客流到达率（人/小时）", 30, 600, p["arrival_rate"], 10)
p["seed"] = st.number_input("随机种子", 0, 9999, p["seed"])

st.success("参数已保存，去「调度运行演示」页面运行仿真。")