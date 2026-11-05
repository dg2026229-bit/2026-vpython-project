box(texture="https://png.pngtree.com/png-vector/20240616/ourmid/pngtree-realistic-human-teeth-and-gums-3d-render-front-view-clipart-png-image_12782549.png")

s1 = sphere(pos=vec(-0.06, 0.105, 0.5), radius=0.017, color=color.black)
s2 = sphere(pos=vec(0.06, -0.09, 0.5), radius=0.017, color=color.black)
s3 = sphere(pos=vec(-0.25, -0.18, 0.5), radius=0.017, color=color.black)

b = box(size = vec(0.1,0.01,0.01), pos = vec(0,0,1))
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
    if 0.1 < b.pos.x < 0.2 and  0.1 < b.pos.y < 0.2  :
        s1.opacity = 0
    if 0.1 < b.pos.x < 0.2 and  0.1 < b.pos.y < 0.2  :
        s2.opacity = 0
    if 0.1 < b.pos.x < 0.2 and  0.1 < b.pos.y < 0.2  :
        s3.opacity = 0
    if 'd' in k : 
        b.pos.x = b.pos.x + 0.01
    if 'a' in k : 
        b.pos.x = b.pos.x - 0.01
    if 'w' in k : 
        b.pos.y = b.pos.y + 0.01
    if 's' in k : 
        b.pos.y = b.pos.y - 0.01
