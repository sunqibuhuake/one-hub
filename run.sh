docker run -d -p 3000:3000 \
  --name one-api \
  --restart always \
  -e TZ=Asia/Shanghai \
  -e USER_TOKEN_SECRET="user_token_secret" \
  -e SESSION_SECRET="session_secret" \
  -v /home/ubuntu/data/one-api:/data \
