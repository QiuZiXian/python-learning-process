from pyecharts.charts import Bar,Page

bar = Bar()
bar.add_xaxis(["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"])
bar.add_yaxis("商家A", [5, 20, 36, 10, 75, 90])
bar1=Bar()
bar1.add_xaxis(["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"])
bar1.add_yaxis("商家A", [5, 20, 36, 10, 75, 90])

page=Page(layout=Page.DraggablePageLayout)
page.add(bar,bar1)
page.render()

