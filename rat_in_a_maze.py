def cango(arr,sx,sy,dx,dy):
    if sx<0 or sy<0 or sx>=row or sy>=col or arr[sx][sy]==0 or vis[sx][sy]==1:
        return 0
    if sx==dx and sy==dy:
        return 1
    vis[sx][sy]=1
    print("ll")
    if cango(arr,sx-1,sy,dx,dy)==1:
        return 1
    if cango(arr,sx,sy-1,dx,dy)==1:
        return 1
    if cango(arr,sx+1,sy,dx,dy)==1:
        return 1
    if cango(arr,sx,sy+1,dx,dy)==1:
        return 1
    return 0
arr=[[1, 0, 1, 1, 0],[1, 1, 1, 0, 1],[0, 1, 0, 1, 1],[1, 1, 1, 1, 0]]
col=len(arr[0])
row=len(arr)
vis=[[0 for i in range(col)] for j in range(row)]
sx,sy=0,0
dx,dy=row-1,col-1
print(vis)
print(cango(arr,sx,sy,dx,dy))
