import http.client

conn = http.client.HTTPSConnection("dev-2l6t2ke8.us.auth0.com")

payload = "{\"client_id\":\"otumjFxstIQQjkUwLjsnZJwQalZafxIo\",\"client_secret\":\"qqipm9ECajwpF9BaVd5cY1JnEVAAExlcW7RcH2CDUQRisTyqU0r4QA7IrTjCp5ii\",\"audience\":\"https://dev-2l6t2ke8.us.auth0.com/api/v2/\",\"grant_type\":\"client_credentials\"}"

headers = { 'content-type': "application/json" }

conn.request("POST", "/oauth/token", payload, headers)

res = conn.getresponse()
data = res.read()
print("ttttt")
print(data.decode("utf-8"))