FROM m.daocloud.io/docker.io/python:slim

# Set working directory and copy project
WORKDIR /adapters

COPY src/ src/
COPY template/ template/
COPY uv.lock .
COPY pyproject.toml .
COPY requirements.txt .
COPY main.py .


# Install project dependencies
RUN pip config set global.index-url https://mirrors.aliyun.com/pypi/simple
RUN pip config set global.trusted-host mirrors.aliyun.com
RUN pip install --upgrade pip --no-cache-dir
RUN pip install uv --no-cache-dir
RUN uv sync --index-url https://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com --no-cache

EXPOSE 8095

# Default command
CMD ["uv", "run", "main.py"]