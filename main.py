import torch

print("=== PyTorch GPU 信息 ===")

# 检查CUDA是否可用
print(f"CUDA 是否可用: {torch.cuda.is_available()}")

if torch.cuda.is_available():
    # 显示GPU数量
    print(f"GPU 数量: {torch.cuda.device_count()}")
    
    # 显示当前GPU设备
    print(f"当前GPU设备: {torch.cuda.current_device()}")
    
    # 显示GPU名称
    for i in range(torch.cuda.device_count()):
        print(f"GPU {i}: {torch.cuda.get_device_name(i)}")
    
    # 显示GPU内存信息
    for i in range(torch.cuda.device_count()):
        memory_allocated = torch.cuda.memory_allocated(i) / 1024**3  # 转换为GB
        memory_reserved = torch.cuda.memory_reserved(i) / 1024**3    # 转换为GB
        print(f"GPU {i} 内存使用: {memory_allocated:.2f}GB (已分配) / {memory_reserved:.2f}GB (已保留)")
    
    # 显示CUDA版本
    print(f"CUDA 版本: {torch.version.cuda}")
    
    # 显示cuDNN版本
    print(f"cuDNN 版本: {torch.backends.cudnn.version()}")
    
else:
    print("没有可用的GPU，将使用CPU")
    print(f"PyTorch 版本: {torch.__version__}")

print("=== 设备信息打印完成 ===") 