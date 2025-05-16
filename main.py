#if not pygame - pip install pygame 
import pygame
import sys
import math
pygame.init()
#[3 -2 1]
#[2 1 -1]
screen  = pygame.display.set_mode((1500,700))
# x,y,w,h = (50,50,50,50)
class rect:
    def __init__(self,name,x,y,z,width,height,wz,dx,dy):
        self.name = name
        self.b = 1
        self.dt = 1
        self.dx,self.dy = dx,dy
        self.x,self.y,self.z = x,y,z
        self.width,self.height,self.wz = width,height,wz

        
        self.change_x = self.x* 1 + self.y * 1 + self.z * 4
        self.change_y = self.x*10+self.y*1+self.z * 0
        
        
        print(self.change_x,self.change_y)
        
       
       
        
        self.pos = [[self.x],
                    [self.y],
                    [self.z]]
      
        self.s = [[8,0],
                  [0,5]]
        self.rolate_2d = [[math.cos(self.b),-math.sin(self.b)],
                       [math.sin(self.b),math.cos(self.b)]]
        self.a = [[3,0,0],
                  [0,3,0],
                  [0,0,3]]
        self.change_3d = [[1,0,0.3],
                          [0,1,0.3],]
        self.rolate()
       
       
        
       
      
    def update(self):
        self.movement()
        self.rolate()
        
      
        self.b += 0.05
        if self.b > 0.05:
           self.b =0
        self.draw()
        self.pos = [[self.x],
                    [self.y],
                    [self.z]]
    def rolate(self):
        self.rolate_y = [[math.cos(self.b),0,math.sin(self.b)],
                          [0,1,0],
                          [-math.sin(self.b),0,math.cos(self.b)]]
        self.rolate_x = [[1,0,0],
                         [0,math.cos(self.b),-math.sin(self.b)],
                         [0,math.sin(self.b),math.cos(self.b)],]
        self.rolate_z = [[math.cos(self.b),-math.sin(self.b),0],
                         [math.sin(self.b),math.cos(self.b),0],
                         [0,0,1]]
    def matrix(self,x,y,z):
        self.change_x = x* 1 + y * 0 + z*(0.5 ) +100 
        self.change_y = x*0 + y*1 + z *(0.1) +100 
    def change(self,matrix,x,y,z):
        self.change_x = x * matrix[0][0] + y * matrix[0][1] + z * matrix[0][2] +self.dx
        self.change_y = x * matrix[1][0] + y * matrix[1][1] + z * matrix[1][2] +self.dy
    def draw(self):
        """
        for x in range(0,self.width,1):
            for y in range(0,self.height,1):
                
                pygame.draw.rect(screen,"white",((self.x+x)*self.s[0][0]+ (self.y+y) *self.s[0][1],
                                                 (self.y+y)*self.s[1][1] +(self.x+x) *self.s[1][0],1,1))
        """
        R = 255
        B = 255
        G = 255
        self.color = (R,B,G)
        for z in range(0,self.width,8):
       
            for y in range(0,self.height,8):
                for x in range(0,self.wz,8):


                    pygame.draw.rect(screen,(255 -x,255-y,255-z),(self.change_x ,self.change_y ,10,10))
                    self.change(self.change_3d,self.x+x,self.y+y,self.z+z)
                        
                
    def cal(self,a,b):
        self.c = [[0,0,0],
                  [0,0,0],
                  [0,0,0]]
        for i in range(len(a)):
            for j in range(len(b[0])):
                    for k in range(len(b)):
                        self.c[i][j] += a[i][k] *b[k][j] 
        #print(self.c)
        self.x = self.c[0][0]
        self.y = self.c[1][0]
        self.z = self.c[2][0]
    def calmatrix(self,a,b,pos = True):
        self.d = [[0,0,0],
                  [0,0,0],
                  ]
        
        
        for i in range(len(a)):
            for j in range(len(b[0])):
                    for k in range(len(b)):
                        if pos:
                            self.d[i][j] += a[i][k] * b[k][j] 
                        else:
                            self.d[i][j] -= a[i][k] * b[k][j] 
        self.change_3d = self.d

    def movement(self):
        
        key =  pygame.key.get_pressed()
        if key[pygame.K_w]:
            self.y -= 1 * self.dt
        if key[pygame.K_a]:
            self.x -=1  * self.dt
        if key[pygame.K_s]:
            self.y += 1  * self.dt
        if key[pygame.K_d]:
            self.x +=1   * self.dt
        
        if key[pygame.K_UP]:
            self.z -=1 * self.dt
        if key[pygame.K_DOWN]:
            self.z +=1 * self.dt
        if key[pygame.K_LSHIFT]:
            self.dt = 20
        else:
            self.dt = 1

        self.calmatrix(self.change_3d,self.rolate_x)
        self.calmatrix(self.change_3d,self.rolate_y)
        #self.calmatrix(self.change_3d,self.rolate_z)

        if key[pygame.K_LCTRL] and key[pygame.K_w]:
            self.calmatrix(self.change_3d,self.rolate_y )
        if key[pygame.K_LCTRL] and key[pygame.K_s]:
            self.calmatrix(self.change_3d,self.rolate_y , False)
        
            
class circle:
    def __init__(self,name,x,y,z,r,dx,dy):
        self.x,self.y,self.z = x,y,z
        self.r =r
        self.dx ,self.dy = dx,dy
        self.name = name

    def update(self):
        self.draw()
    def draw(self):
        for i in range(1,360,1):
            pygame.draw.rect(screen,"white",(self.r*math.cos(i) +500,self.r*math.sin(i)+300,1,1))
                
                
                
   
fps = 60
clock = pygame.time.Clock()
p_ = []
for i in range(0,5,1):
    p = rect("p1",250,-500 + (i* 250),50,200,200,200,0,0)
    p_.append(p)
b = rect('p2',150,200,200,200,200,240,500,0)
#c = circle('c1',100,100,100,50,0,0)
while True:
    clock.tick(fps)
    screen.fill('black')
    b.update()
    #c.update()
    
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
