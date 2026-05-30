# # print("请输入半径r")
# # r=float(input())
# # pi=3.14
# # Area=3.14*r**2
# # print(f'圆的面积为：{Area:.2f}')
#
# #
# # import pandas as pd
# # import numpy as np
# # # 读取数据
# # df = pd.read_excel(r'编程作业数据表.xlsx', sheet_name=0,
# #     converters={'年':str, '月':str})
# # # 筛选公司编号为10158
# # df10158 = df[df['公司'] == 10158].reset_index(drop=True)
# #
# # # 提取各列数据
# # cost = df10158['营业成本'].fillna(0)
# # profit_total = df10158['利润总额'].fillna(0)
# # profit_net = df10158['净利润'].fillna(0)
# # assets = df10158['资产合计'].fillna(1)
# # equity = df10158['权益合计'].fillna(1)
# #
# # # 计算财务指标
# # # 资产净利率 = 净利润 / 资产合计
# # roa = profit_net / assets
# # # 权益净利率 = 净利润 / 权益合计
# # roe = profit_net / equity
# # # 利润率(基于资产) = 利润总额 / 资产合计
# # profit_margin = profit_total / assets
# #
# #
# # # 企业两年的销量对比图（使用资产合计数据）
# # months = ['Jan','Feb','Mar','Apr','May','Jun',
# #           'Jul','Aug','Sep','Oct','Nov','Dec']
# # asset_2018 = assets[year=='2018'].tolist()
# # asset_2019 = assets[year=='2019'].tolist()
# #
# # x = np.arange(len(months))
# # width = 0.35
# # fig, ax = plt.subplots(figsize=(10, 5))
# # ax.bar(x - width/2, asset_2018, width, label='2018年', color='#E74C3C')
# # ax.bar(x + width/2, asset_2019, width, label='2019年', color='#3498DB')
# # ax.set_title('公司10158两年资产合计对比')
# # ax.set_xticks(x)
# # ax.set_xticklabels(months)
# # ax.legend()
# # plt.show()
# #
# #
# # # 2018年各指标利率统计折线图
# # roa_18 = roa[year=='2018'].tolist()
# # roe_18 = roe[year=='2018'].tolist()
# # pm_18 = profit_margin[year=='2018'].tolist()
# #
# # fig, ax = plt.subplots(figsize=(10, 5))
# # ax.plot(months, roa_18, marker='o', label='资产净利率')
# # ax.plot(months, roe_18, marker='s', label='权益净利率')
# # ax.plot(months, pm_18, marker='^', label='利润率')
# # ax.set_title('2018年公司各指标利率统计')
# # ax.legend()
# # ax.grid(axis='y', linestyle='--')
# # plt.show()
# #
# #
# #
# # # 2019年各指标利率统计折线图
# # months_19 = ['Jan','Feb','Mar','Apr','May','Jun',
# #              'Jul','Aug','Sep','Oct']
# # roa_19 = roa[year=='2019'].tolist()
# # roe_19 = roe[year=='2019'].tolist()
# # pm_19 = profit_margin[year=='2019'].tolist()
# #
# # fig, ax = plt.subplots(figsize=(10, 5))
# # ax.plot(months_19, roa_19, marker='o', label='资产净利率')
# # ax.plot(months_19, roe_19, marker='s', label='权益净利率')
# # ax.plot(months_19, pm_19, marker='^', label='利润率')
# # ax.set_title('2019年公司各指标利率统计')
# # ax.legend()
# # ax.grid(axis='y', linestyle='--')
# # plt.show()
#
# # 公司月资产玫瑰饼图
# # from pyecharts.charts import Pie
# # from pyecharts import options as opts
# # from pyecharts.globals import ThemeType
# #
# # monthly = assets.groupby(month).sum()
# # pie = (
# #     Pie(init_opts=opts.InitOpts(theme=ThemeType.DARK))
# #     .add('', [list(z) for z in zip(monthly.index,
# #               monthly.values)], rosetype='radius'
# #     )
# #     .set_global_opts(
# #         title_opts=opts.TitleOpts(
# #         title='公司10158月资产玫瑰饼图')
# #     )
# # )
# # pie.render_notebook()
# # import pandas as pd
# # import numpy as np
# # # 读取数据
# # df = pd.read_excel(r'编程作业数据表.xlsx', sheet_name=0,
# #     converters={'年':str, '月':str})
# # # 筛选公司编号为10158
# # df10158 = df[df['公司'] == 10158].reset_index(drop=True)
#
# # # 提取各列数据
# # cost = df10158['营业成本'].fillna(0)
# # profit_total = df10158['利润总额'].fillna(0)
# # profit_net = df10158['净利润'].fillna(0)
# # assets = df10158['资产合计'].fillna(1)
# # equity = df10158['权益合计'].fillna(1)
# #
# # # 计算财务指标
# # # 资产净利率 = 净利润 / 资产合计
# # roa = profit_net / assets
# # # 权益净利率 = 净利润 / 权益合计
# # roe = profit_net / equity
# # # 利润率(基于资产) = 利润总额 / 资产合计
# # profit_margin = profit_# 提取各列数据
# # cost = df10158['营业成本'].fillna(0)
# # profit_total = df10158['利润总额'].fillna(0)
# # profit_net = df10158['净利润'].fillna(0)
# # assets = df10158['资产合计'].fillna(1)
# # equity = df10158['权益合计'].fillna(1)
# #
# # # 计算财务指标
# # # 资产净利率 = 净利润 / 资产合计
# # roa = profit_net / assets
# # # 权益净利率 = 净利润 / 权益合计
# # roe = profit_net / equity
# # # 利润率(基于资产) = 利润总额 / 资产合计
# # profit_margin = profit_total / assetstotal / assets
#
# # 企业两年的销量对比图（使用资产合计数据）
# months = ['Jan','Feb','Mar','Apr','May','Jun',
#           'Jul','Aug','Sep','Oct','Nov','Dec']
# asset_2018 = assets[year=='2018'].tolist()
# asset_2019 = assets[year=='2019'].tolist()
#
# x = np.arange(len(months))
# width = 0.35
# fig, ax = plt.subplots(figsize=(10, 5))
# ax.bar(x - width/2, asset_2018, width, label='2018年', color='#E74C3C')
# ax.bar(x + width/2, asset_2019, width, label='2019年', color='#3498DB')
# ax.set_title('公司10158两年资产合计对比')
# ax.set_xticks(x)
# ax.set_xticklabels(months)
# ax.legend()
# plt.show()
#
# # 2018年各指标利率统计折线图
# roa_18 = roa[year=='2018'].tolist()
# roe_18 = roe[year=='2018'].tolist()
# pm_18 = profit_margin[year=='2018'].tolist()
#
# fig, ax = plt.subplots(figsize=(10, 5))
# ax.plot(months, roa_18, marker='o', label='资产净利率')
# ax.plot(months, roe_18, marker='s', label='权益净利率')
# ax.plot(months, pm_18, marker='^', label='利润率')
# ax.set_title('2018年公司各指标利率统计')
# ax.legend()
# ax.grid(axis='y', linestyle='--')
# plt.show()
#
# # 2019年各指标利率统计折线图
# months_19 = ['Jan','Feb','Mar','Apr','May','Jun',
#              'Jul','Aug','Sep','Oct']
# roa_19 = roa[year=='2019'].tolist()
# roe_19 = roe[year=='2019'].tolist()
# pm_19 = profit_margin[year=='2019'].tolist()
#
# fig, ax = plt.subplots(figsize=(10, 5))
# ax.plot(months_19, roa_19, marker='o', label='资产净利率')
# ax.plot(months_19, roe_19, marker='s', label='权益净利率')
# ax.plot(months_19, pm_19, marker='^', label='利润率')
# ax.set_title('2019年公司各指标利率统计')
# ax.legend()
# ax.grid(axis='y', linestyle='--')
# plt.show()
#
#
# # 公司月资产玫瑰饼图
# from pyecharts.charts import Pie
# from pyecharts import options as opts
# from pyecharts.globals import ThemeType
#
# monthly_assets = assets.groupby(month).sum()
# pie = (
#     Pie(init_opts=opts.InitOpts(theme=ThemeType.DARK))
#     .add('', [list(z) for z in zip(monthly_assets.index,
#               monthly_assets.values)], rosetype='radius')
#     .set_global_opts(
#         title_opts=opts.TitleOpts(
#             title='公司10158月资产玫瑰饼图'))
# )
# pie.render_notebook()