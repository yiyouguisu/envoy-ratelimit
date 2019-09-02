# Network Layer

## 发送10个请求，结果只有5个请求完成了，与配置文件对应

```yaml
  - key: name
    value: xixi
    rate_limit:
      unit: second
      requests_per_unit: 5
```


```shell
siege -c 1 -r 10 -v -H "name:xixi"  http://localhost:8090/service
** SIEGE 4.0.4
** Preparing 1 concurrent users for battle.
The server is now under siege...
HTTP/1.1 200     0.05 secs:      10 bytes ==> GET  /service
HTTP/1.1 200     0.06 secs:      10 bytes ==> GET  /service
HTTP/1.1 200     0.03 secs:      10 bytes ==> GET  /service
HTTP/1.1 200     0.04 secs:      10 bytes ==> GET  /service
HTTP/1.1 200     0.01 secs:      10 bytes ==> GET  /service

Transactions:		           5 hits
Availability:		       50.00 %
Elapsed time:		        0.22 secs
Data transferred:	        0.00 MB
Response time:		        0.04 secs
Transaction rate:	       22.73 trans/sec
Throughput:		        0.00 MB/sec
Concurrency:		        0.86
Successful transactions:           5
Failed transactions:	           5
Longest transaction:	        0.06
Shortest transaction:	        0.01

```

## 修改运行时配置，禁用全局限流

```shell
curl -X POST http://localhost:9901/runtime_modify?ratelimit.tcp_filter_enabled=0

```

## 发送10个请求，结果10个请求都完成了

```shell
siege -c 1 -r 10 -v -H "name:xixi"  http://localhost:8090/service                 
** SIEGE 4.0.4
** Preparing 1 concurrent users for battle.
The server is now under siege...
HTTP/1.1 200     0.01 secs:      10 bytes ==> GET  /service
HTTP/1.1 200     0.02 secs:      10 bytes ==> GET  /service
HTTP/1.1 200     0.01 secs:      10 bytes ==> GET  /service
HTTP/1.1 200     0.01 secs:      10 bytes ==> GET  /service
HTTP/1.1 200     0.01 secs:      10 bytes ==> GET  /service
HTTP/1.1 200     0.00 secs:      10 bytes ==> GET  /service
HTTP/1.1 200     0.01 secs:      10 bytes ==> GET  /service
HTTP/1.1 200     0.02 secs:      10 bytes ==> GET  /service
HTTP/1.1 200     0.01 secs:      10 bytes ==> GET  /service
HTTP/1.1 200     0.01 secs:      10 bytes ==> GET  /service

Transactions:		          10 hits
Availability:		      100.00 %
Elapsed time:		        0.12 secs
Data transferred:	        0.00 MB
Response time:		        0.01 secs
Transaction rate:	       83.33 trans/sec
Throughput:		        0.00 MB/sec
Concurrency:		        0.92
Successful transactions:          10
Failed transactions:	           0
Longest transaction:	        0.02
Shortest transaction:	        0.00

```


# Http Layer

## 发送10个请求，只有5个请求完成了，其他请求返回429

```shell
siege -c 1 -r 10 -v -H "name:xixi"  http://localhost:8081/service   
** SIEGE 4.0.4
** Preparing 1 concurrent users for battle.
The server is now under siege...
HTTP/1.1 200     0.03 secs:      10 bytes ==> GET  /service
HTTP/1.1 200     0.03 secs:      10 bytes ==> GET  /service
HTTP/1.1 200     0.02 secs:      10 bytes ==> GET  /service
HTTP/1.1 200     0.02 secs:      10 bytes ==> GET  /service
HTTP/1.1 200     0.05 secs:      10 bytes ==> GET  /service
HTTP/1.1 429     0.01 secs:       0 bytes ==> GET  /service
HTTP/1.1 429     0.01 secs:       0 bytes ==> GET  /service
HTTP/1.1 429     0.01 secs:       0 bytes ==> GET  /service
HTTP/1.1 429     0.01 secs:       0 bytes ==> GET  /service
HTTP/1.1 429     0.01 secs:       0 bytes ==> GET  /service

Transactions:		          10 hits
Availability:		      100.00 %
Elapsed time:		        0.20 secs
Data transferred:	        0.00 MB
Response time:		        0.02 secs
Transaction rate:	       50.00 trans/sec
Throughput:		        0.00 MB/sec
Concurrency:		        1.00
Successful transactions:           5
Failed transactions:	           0
Longest transaction:	        0.05
Shortest transaction:	        0.01

```

## 修改运行时配置，禁用http限流

```shell
curl -X POST http://localhost:9901/runtime_modify?ratelimit.http_filter_enabled=0

```

## 发送10个请求，结果请求全部完成了

```shell
siege -c 1 -r 10 -v -H "name:xixi"  http://localhost:8081/service                  
** SIEGE 4.0.4
** Preparing 1 concurrent users for battle.
The server is now under siege...
HTTP/1.1 200     0.01 secs:      10 bytes ==> GET  /service
HTTP/1.1 200     0.01 secs:      10 bytes ==> GET  /service
HTTP/1.1 200     0.03 secs:      10 bytes ==> GET  /service
HTTP/1.1 200     0.05 secs:      10 bytes ==> GET  /service
HTTP/1.1 200     0.05 secs:      10 bytes ==> GET  /service
HTTP/1.1 200     0.02 secs:      10 bytes ==> GET  /service
HTTP/1.1 200     0.01 secs:      10 bytes ==> GET  /service
HTTP/1.1 200     0.03 secs:      10 bytes ==> GET  /service
HTTP/1.1 200     0.02 secs:      10 bytes ==> GET  /service
HTTP/1.1 200     0.01 secs:      10 bytes ==> GET  /service

Transactions:		          10 hits
Availability:		      100.00 %
Elapsed time:		        0.25 secs
Data transferred:	        0.00 MB
Response time:		        0.02 secs
Transaction rate:	       40.00 trans/sec
Throughput:		        0.00 MB/sec
Concurrency:		        0.96
Successful transactions:          10
Failed transactions:	           0
Longest transaction:	        0.05
Shortest transaction:	        0.01

```