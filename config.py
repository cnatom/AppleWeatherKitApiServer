import time

import jwt


class Config:
    def __init__(self):
        self.key_id = "DQ362YMNMP"
        self.team_id = "95VT929YHJ"
        self.service_id = "com.bytedance.ssr"
        self.private_key = open("./static/AuthKey_DQ362YMNMP.p8").read()
        self.cur_time = int(time.time())
        self.expiry = (int(time.time()) + 1000)
        self.algorithm = "ES256"

    def genToken(self):
        payload = self.__getPayload()
        private_key = self.private_key
        algorithm = "ES256"
        headers = self.__getHeaders()
        print(payload)
        print(headers)
        encoded_jwt = jwt.encode(payload=payload, key=private_key, algorithm=algorithm, headers=headers)
        return encoded_jwt

    def __getPayload(self):
        return {"iss": self.team_id, "iat": self.cur_time, "exp": self.expiry, "sub": self.service_id}

    def __getHeaders(self):
        return {"kid": self.key_id, "id": (self.team_id + '.' + self.service_id), "alg": self.algorithm}
