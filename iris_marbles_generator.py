import bpy

from sklearn.datasets import load_iris
import numpy as np

data = load_iris()

X = data.data

count = 0
total = 0
loop_x = 0

mat1 = bpy.data.materials.get("flower1")
mat2 = bpy.data.materials.get("flower2")
mat3 = bpy.data.materials.get("flower3")

numbers = np.arange(150)
np.random.shuffle(numbers)

for i in numbers:
  flower = X[i]
  total +=1
  count +=1
  
  print(flower[0])
  
  width = (flower[2]/5)+1
  length = (flower[3]-.8)/1.8
  
  bpy.ops.mesh.primitive_uv_sphere_add(segments=16, 
  ring_count=8,  
  radius=width, 
  enter_editmode=False, 
  
  location=(0, loop_x*2, count*5))
  
  bpy.ops.rigidbody.object_add()
  bpy.context.object.rigid_body.friction = 0.1
  bpy.context.object.rigid_body.collision_shape = 'SPHERE'
  if i <= 50:
    bpy.context.object.data.materials.append(mat1)
  elif i <= 100:
    bpy.context.object.data.materials.append(mat2)
  else:
    bpy.context.object.data.materials.append(mat3)
  
  bounce = length
  bpy.ops.object.shade_smooth()
  bpy.context.object.rigid_body.restitution = bounce
  if (count%10) == 0:
       loop_x += 3
       count = 0
