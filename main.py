Web VPython 3.2
box(texture="https://png.pngtree.com/png-vector/20240616/ourmid/pngtree-realistic-human-teeth-and-gums-3d-render-front-view-clipart-png-image_12782549.png")

s1 = sphere(pos=vec(-0.06, 0.105, 0.5), radius=0.017, color=color.black)
s2 = sphere(pos=vec(0.06, -0.09, 0.5), radius=0.017, color=color.black)
s3 = sphere(pos=vec(-0.25, -0.18, 0.5), radius=0.017, color=color.black)

brush_head = box(pos=vec(0, 0, 0), length=0.5, height=0.3, width=0.2, color=color.cyan)
brush_body = box(pos=vec(0, 0, 0), length=0.5, height=0.3, width=0.2, color=color.cyan)

brush = compound([brush_head, brush_body])

b = box(size = vec(0.135,0.02,0.01), pos = vec(1,-0.02,1))
while True :
    rate(100)
    k = keysdown()
    if b.pos.x > 0.2 : 
        b.pos.x = 0.2
    if b.pos.x < -0.2 : 
        b.pos.x = -0.2
    if b.pos.y > 0.2 : 
        b.pos.y = 0.2
    if b.pos.y < -0.2 : 
        b.pos.y = -0.2
        
    if -0.08 < b.pos.x < 0 and 0.04 < b.pos.y < 0.07  :
        s1.opacity = 0
    if -0.04 < b.pos.x < 0.1 and  -0.08 < b.pos.y < -0.03  :
        s2.opacity = 0
    if -0.2 < b.pos.x < -0.07 and  -0.1 < b.pos.y < -0.05  :
        s3.opacity = 0
    if 'd' in k : 
        b.pos.x = b.pos.x + 0.01
    if 'a' in k : 
        b.pos.x = b.pos.x - 0.01
    if 'w' in k : 
        b.pos.y = b.pos.y + 0.01
    if 's' in k : 
        b.pos.y = b.pos.y - 0.01
