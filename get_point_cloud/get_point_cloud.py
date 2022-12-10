import imageio.v3 as iio
import numpy as np
import matplotlib.pyplot as plt
import open3d as o3d

depth_image=iio.imread("captures\depth.png")

#printing properties
print(f"image shape is : {depth_image.shape}")
print(f"image datatype is : {depth_image.dtype}")
print(f"min depth is :{np.argmin(depth_image)}")
print(f"max depth is : {np.argmax(depth_image)}")


#getting camera parameters
'''f_x=5.31147360e+03
f_y=5.33846841e+03
c_x=2.64132939e+03
c_y=2.05551027e+03'''

FX_DEPTH = 5.8262448167737955e+02
FY_DEPTH = 5.8269103270988637e+02
CX_DEPTH = 3.1304475870804731e+02
CY_DEPTH = 2.3844389626620386e+02

#computing point cloud

pcd=[]
height,width=depth_image.shape

for i in range(height):
    for j in range(width):
        z=depth_image[i][j]
        x=(j-CX_DEPTH)*z/FX_DEPTH
        y=(i-CY_DEPTH)*z/FY_DEPTH
        pcd.append([x,y,z])

#displaying point cloud

pcd_o3d=o3d.geometry.PointCloud()
pcd_o3d.points=o3d.utility.Vector3dVector(pcd)

o3d.visualization.draw_geometries([pcd_o3d])