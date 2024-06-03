import jieba
import wordcloud

f = open("world.txt", "r", encoding="utf-8")

t = f.read()
f.close()
ls = jieba.lcut(t)

txt = " ".join(ls)
w = wordcloud.WordCloud( \
    width=1920, height=1080, \
    background_color="white",
    font_path="msyh.ttc"
)
w.generate(txt)
w.to_file("grwordcloud.png")