import time

import jwt


class JwtConfig:
    def __init__(self):
        self.token = ""
        self.key_id = "DQ362YMNMP"
        self.team_id = "95VT929YHJ"
        self.service_id = "com.bytedance.ssr"
        self.private_key = open("./static/AuthKey_DQ362YMNMP.p8").read()
        self.cur_time = int(time.time())
        self.expiry = (int(time.time()) + 3600)
        self.algorithm = "ES256"

    def genToken(self):
        # 如果token没有初始化 or token过期了 => 生成新的token
        if self.token == "" or self.__tokenAlreadyExpired():
            self.cur_time = int(time.time())
            self.expiry = (int(time.time()) + 1000)
            payload = self.__getPayload()
            private_key = self.private_key
            algorithm = "ES256"
            headers = self.__getHeaders()
            self.token = jwt.encode(payload=payload, key=private_key, algorithm=algorithm, headers=headers)
        return self.token

    def __tokenAlreadyExpired(self) -> bool:
        return int(time.time()) > self.expiry

    def __getPayload(self) -> dict:
        return {"iss": self.team_id, "iat": self.cur_time, "exp": self.expiry, "sub": self.service_id}

    def __getHeaders(self) -> dict:
        return {"kid": self.key_id, "id": (self.team_id + '.' + self.service_id), "alg": self.algorithm}
