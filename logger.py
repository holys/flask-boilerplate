import logging

# 创建 logger 对象
logger = logging.getLogger("flask.app")

# 设置日志级别为 INFO
logger.setLevel(logging.INFO)

# 创建文件 handler，将日志写入到文件中
file_handler = logging.FileHandler("flask.log")
file_handler.setLevel(logging.INFO)

# 设置日志格式
formatter = logging.Formatter("%(asctime)s %(levelname)s: %(message)s")
file_handler.setFormatter(formatter)

# 添加 handler 到 logger 对象中
logger.addHandler(file_handler)
