# 迷宫问题：
# https://www.nowcoder.com/practice/cf24906056f4488c9ddb132f317e03bc?
# tpId=389&tqId=36867&sourceUrl=%2Fexam%2Foj
h,w=map(int,input().split())
arr=[input().split()for i in range(h)]
path=[]
def maze(x,y,arr,path):
    # 1. 能走吗？（没出界 + 不是墙)
    if 0<=x<len(arr) and 0<=y<len(arr[0]) and arr[x][y]=="0":
        # 2. 记录这一步
        path.append((x,y))
        # 3.到头了？
        if x==len(arr)-1 and y==len(arr[0])-1:
            return path
        # 4. 标记走过了（变成墙，防止重复走）
        arr[x][y]="1"
        # 5. 往四个方向试
        for dx,dy in[(-1,0), (1,0), (0,-1), (0,1)]:
            new_path=maze(dx+x,dy+y,arr,path)
            if new_path:
                return new_path
    return None

path=maze(0,0,arr,path)
if path:
    for i in path:
        print(f"({i[0]},{i[1]})")