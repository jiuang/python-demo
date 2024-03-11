import paddlehub as hub
# import paddle.fluid as fluid

model = hub.Module(name="lac")
text = "请介绍一下鹏博集团"
keywords = model.keyword_extraction(text=text)
print(keywords)