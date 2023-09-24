from PIL import Image
import numpy as np
import matplotlib.pyplot as plt 


file_name = r'C:\Users\sandr\OneDrive\Documents\Zavrsni\Slike\akusticna_g.png'
def matrica():
    image = Image.open(file_name)
    image=image.convert("RGB")
    Gitara = np.array(image)
    print(Gitara.shape)

    w,h,rgb=Gitara.shape

    #plt.imshow(Gitara)
    #plt.show()


        #napravit novu matricu di su svi bili 0 a sve sta nije bilo slobonda vrijednost
        #ili pronaci na koji sve pixeli su 0 pa napravit konstanto pripravljati tj applyat pocetne uvjete

    Shape_matrix=np.zeros((w,h)) #Pravi 2D kvadratnu matricu u kojoj ce 
        #biti nacrtan oblik gitare  


    for x in range(w):
        for y in range(h):
            pixel = image.getpixel((x,y))  
            if pixel==(255,255,255):         
                Shape_matrix[x,y]=1
            if pixel==(255,0,0):
                Shape_matrix[x,y]=2
            if pixel==(0,0,0):
                Shape_matrix[x,y]=3        
        

    flag=True
    if flag==True:
        plt.imshow(Shape_matrix, cmap='viridis')  
        plt.colorbar()
        plt.show()

    return Shape_matrix

#gitara=matrica()
#print(gitara[0,0])
matrica()