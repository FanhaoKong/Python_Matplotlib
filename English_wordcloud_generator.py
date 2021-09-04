import imageio as im
import wordcloud as w
name=input("Please input the name and the address of the txt file:\n")
file=open(name,"rt",encoding="utf-8")
a=file.read()
stop={"including","these","that","part","based","to","and","in", \
      "as","we","of","is","We","the","was","were","therefore","because","our"}
name2=input("Please input the name and the address of the background picture:\n")
mask1=im.imread(name2)
cloud=w.WordCloud(width=2048,height=1536,background_color="white",mask=mask1, \
                  stopwords=stop)
cloud.generate(a)
cloud.to_file("E:/360MoveData/Users/kongf/Desktop/cloud.jpg")
