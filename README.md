# PyTorch Docker 示例 (GPU信息检测)

这是一个简单的PyTorch项目示例，演示了如何使用Docker运行PyTorch代码并检测GPU设备信息。

## 项目内容

- `main.py`: GPU设备信息检测脚本
- `requirements.txt`: Python依赖文件
- `Dockerfile`: Docker配置文件（基于PyTorch官方CUDA镜像）

## 系统要求

- Docker
- NVIDIA GPU (可选，如果没有GPU会显示CPU信息)
- NVIDIA Docker运行时 (nvidia-docker2)

## 使用方法

### 1. 安装NVIDIA Docker运行时
可参看文章：[《第二部分：Docker GPU 容器实战指南》](https://blog.lusyoe.com/article/docker-gpu-guide)

### 2. 构建Docker镜像
```bash
docker build -t pytorch-example-gpu .
```

### 3. 运行容器（GPU模式）
```bash
docker run --gpus all pytorch-example-gpu
```

## 示例输出

运行后你会看到类似这样的输出：
```
=== PyTorch GPU 信息 ===
CUDA 是否可用: True
GPU 数量: 1
当前GPU设备: 0
GPU 0: NVIDIA GeForce RTX 3080
GPU 0 内存使用: 0.00GB (已分配) / 0.00GB (已保留)
CUDA 版本: 12.1
cuDNN 版本: 8902
=== 设备信息打印完成 ===
```

如果没有GPU，输出会是：
```
=== PyTorch GPU 信息 ===
CUDA 是否可用: False
没有可用的GPU，将使用CPU
PyTorch 版本: 2.2.2
=== 设备信息打印完成 ===
```

## 检测的信息

- CUDA可用性
- GPU数量和名称
- GPU内存使用情况
- CUDA和cuDNN版本
- PyTorch版本

这个示例可以帮助你验证Docker容器中的GPU配置是否正确。

## 许可证

本项目采用 [MIT 协议](LICENSE) 进行许可。 