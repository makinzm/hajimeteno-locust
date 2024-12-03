FROM ghcr.io/astral-sh/uv:python3.13-alpine

# 必要なビルドツールをインストール
RUN apk add --no-cache gcc python3-dev musl-dev linux-headers

# pyproject.toml をコンテナ内にコピー
COPY pyproject.toml /app/pyproject.toml

WORKDIR /app

RUN uv sync

COPY src /app/src
COPY proto /app/proto

# 必要なポートを公開
EXPOSE 8089

# コマンドを実行
CMD ["uv", "run", "src/main.py"]
