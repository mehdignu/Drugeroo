#!/usr/bin/env python3

import pusher

pusher_client = pusher.Pusher(
  app_id="351287",
  key="b91115f15fb79204ed0d",
  secret="1267c358e31740c55933",
  cluster="eu",
  ssl=True,
authEndpoint="https://secure-temple-86252.herokuapp.com/pusher/auth"
)

pusher_client.trigger("private-my-channel", "client-my-event", {"message": "hello world"})
