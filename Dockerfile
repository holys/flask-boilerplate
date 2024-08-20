FROM python:3.8

WORKDIR /app

# Timezone for China
RUN ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime

# For Chinese users to accelerate the installation of Python packages
ENV \
  PIP_INDEX_URL=https://mirrors.aliyun.com/pypi/simple/ \
  PIP_TRUSTED_HOST=mirrors.aliyun.com

# Install Python dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 6000

CMD ["python", "app.py"]