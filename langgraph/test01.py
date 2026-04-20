from typing import TypedDict, Annotated
from operator import add

from langgraph.constants import START, END
from langgraph.graph import StateGraph


# 1. 定义包裹状态（只定义一次，无重复）
class PackageState(TypedDict):
    package_id: str          # 包裹id
    origin: str              # 始发站
    destination: str         # ⽬的地
    status: str              # 待揽收/运输中/派送中/已签收
    history: Annotated[list[str], add]  # 流转历史
    total_distance: Annotated[int, add]  # 总⾥程
    priority: str            # 普通/加急


# 2. 构建流程图
delivery = StateGraph(PackageState)

# 3. 定义节点函数（只写一次）
def receive_package(state: PackageState):
    """揽收站"""
    return {
        "status": "已揽收",
        "history": [f"在{state['origin']}揽收"]
    }

def sort_package(state: PackageState):
    """分拣中⼼"""
    destination = state["destination"]
    if "北京" in destination:
        next_station = "北京分拣中⼼"
    elif "上海" in destination:
        next_station = "上海分拣中⼼"
    else:
        next_station = "其他地区分拣中�中心"
    return {
        "status": "已分拣",
        "history": [f"分拣⾄{next_station}"]
    }

def standard_delivery(state: PackageState):
    """标准配送"""
    return {
        "status": "运输中",
        "history": ["标准陆运"],
        "total_distance": 500
    }

def express_delivery(state: PackageState):
    """加急配送"""
    return {
        "status": "加急运输",
        "history": ["空运加急"],
        "total_distance": 800
    }

def final_delivery(state: PackageState):
    """派送站"""
    return {
        "status": "已签收",
        "history": [f"已送达{state['destination']}"]
    }


# 4. 添加节点（只添加一次）
delivery.add_node("揽收站", receive_package)
delivery.add_node("分拣中心", sort_package)
delivery.add_node("标准配送", standard_delivery)
delivery.add_node("加急配送", express_delivery)
delivery.add_node("派送站", final_delivery)


# 5. 智能路由：只写一次正确的逻辑
def select_delivery(state: PackageState):
    if state["priority"] == "加急":
        return "加急配送"
    else:
        return "标准配送"

# 6. 连接流程（正确路线）
delivery.add_edge(START, "揽收站")
delivery.add_edge("揽收站", "分拣中心")

# 条件边：分拣中心 → 根据优先级走标准/加急
delivery.add_conditional_edges(
    "分拣中心",
    select_delivery,
    ["标准配送", "加急配送"]
)

delivery.add_edge("标准配送", "派送站")
delivery.add_edge("加急配送", "派送站")
delivery.add_edge("派送站", END)

# 7. 编译
delivery_system = delivery.compile()

# 8. 测试
test_packages = [
    {
        "package_id": "P001",
        "origin": "北京",
        "destination": "上海",
        "priority": "普通",
        "history": [],
        "total_distance": 0
    },
    {
        "package_id": "P002",
        "origin": "⼴州",
        "destination": "乌鲁⽊⻬",
        "priority": "加急",
        "history": [],
        "total_distance": 0
    }
]

for package in test_packages:
    print(f"\n===== 配送包裹: {package['package_id']} =====")
    result = delivery_system.invoke(package)
    print("最终状态:", result["status"])
    print("配送历史:", result["history"])
    print("总⾥程:", result["total_distance"])