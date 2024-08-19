import matplotlib.pyplot as plt
import numpy as np

# xpoints = np.array([1,2,3,4,5,6])
# ypoints = np.array([7,8,9,1,2,3])
# x= np.array(['A','B','c','D'])
# y= np.array([15,20,30,60])
# z= np.array(['blue' , 'red' , 'green' , 'black'])
# colors = np.array([7,8,9,1])


# xpoints1 = np.array([0,1,5])
# ypoints1 = np.array([0,6,5])


# plt.plot(xpoints,ypoints , "*:y") # yellow color star pointed line graph 
# plt.plot(ypoints , "o")  # line graph with marked point
# plt.plot(ypoints , "y") # line graph with yellow color
# plt.plot(ypoints , ":") # doted line graph 
# plt.plot(ypoints , "*" , ms=20)
# plt.plot(ypoints ,linestyle = 'dashed',linewidth=0.5 , ms=20 , mec='r' , mfc='g' , color='#4287f5')
# plt.bar(xpoints,ypoints)
# mfc = marker face color
# mec = marker outer color
# ms =  maker size


# plt.xlabel("Data")
# plt.ylabel("output")
# plt.title("Graph data")
# plt.grid(color='red' , linewidth = 0.5 , linestyle='--')


# plt.subplot(2,2,1)
# plt.plot(xpoints1 , ypoints1 )

# plt.subplot(2,2,2)

# plt.plot(xpoints1 , ypoints1 )

# plt.scatter(xpoints , ypoints , c=colors)
# plt.barh(x,y , color='red' )
# lines = plt.plot(x1, y1, x2, y2)
# plt.bar(x,y , color = z)
# plt.setp(lines, 'color', 'r', 'linewidth', 2.0)


# x = np.random.normal(170 ,10,250)
# plt.hist(x)

x = np.array([10,15,25,30,20])
ex = np.array([0.1,0,0,0.1,0.1])
l = np.array(["Facebook","Google","Open AI","Gemini","Midjerny"])
plt.pie(x,labels=l ,explode=ex)
plt.legend(l)
plt.show()

# print(xpoints)