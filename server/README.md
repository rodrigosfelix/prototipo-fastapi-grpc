# prototipo-fastapi-grpc

commands: 
```shell
python3.12 -m grpc_tools.protoc --proto_path=./protos --python_out=./generated --pyi_out=./generated --grpc_python_out=./generated protos/bar.proto
```