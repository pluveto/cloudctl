cloudctl 致力于设计一套通用的云服务器管理接口，并提供通用的云服务器管理功能，如：开机、查看状态、重启。

## 支持的云服务商

+ 华为云 `huawei`

## 使用方法

### 配置运行环境

```shell
# 克隆仓库
git clone https://github.com/pluveto/cloudctl
cd cloudctl
# 创建虚拟环境
python -m venv ./venv
./venv/Scripts/activate
# 安装依赖
python -m pip install -r requirement.txt
```

### 配置

创建 `.env` 文件，填写认证信息。示例：

```shell
LOG_LEVEL=info
HUAWEICLOUD_SDK_AK=KAAABBCCDABABABABABAB
HUAWEICLOUD_SDK_SK=111111111111QQQQQQQQQQQQQqqqqqqqqfffffff
HUAWEICLOUD_SDK_PROJECT_ID=0df51c3c6400f4c52fbe8888888888888
HUAWEICLOUD_SDK_IAM_ENDPOINT=ecs.cn-north-4.myhuaweicloud.com
```

创建 `config.yaml` 文件，填写服务器信息。示例：

```yaml
servers:
  - id: 38210be0-80ee-46f5-81ad-4ed2839309c6
    provider: huawei
  - id: 1dd9d8d5-bf9d-4810-a303-3a7244ea5ede
    provider: huawei
  - id: 6de462db-bb8c-44ee-b120-03c5268cce44
    provider: huawei
  - id: b46113d6-d570-4691-a1ed-7a6b8d4e57a7
    provider: huawei
```

### 使用

```shell
# 列出所有服务器
py cloudctl.py server --action list
# 批量开机
py cloudctl.py server --action start --server-ids 38210be0-80ee-46f5-81ad-4ed2839309c6 1dd9d8d5-bf9d-4810-a303-3a7244ea5ede 6de462db-bb8c-44ee-b120-03c5268cce44 b46113d6-d570-4691-a1ed-7a6b8d4e57a7
# 批量关机
py cloudctl.py server --action stop --server-ids 38210be0-80ee-46f5-81ad-4ed2839309c6 1dd9d8d5-bf9d-4810-a303-3a7244ea5ede 6de462db-bb8c-44ee-b120-03c5268cce44 b46113d6-d570-4691-a1ed-7a6b8d4e57a7
```

### 华为云相关凭证的获取

访问 https://support.huaweicloud.com/devg-apisign/api-sign-provide.html

## 扩展

本项目可以自行扩展支持其它服务商。只需要在 `extensions` 目录下建立文件 `PROVIDER_NAME.py`

### 调用约定

你的扩展需要实现以下方法。返回值均为 dict 类型。
<!-- 
#### get_server_status
参数：
 + 无
返回： -->
#### list_servers

参数：
 + 无

返回：
 + Array of: 
   + `id: string`
   + `status: string`
   + `name: string`
   + `private_ip: string`
   + `public_ip: string`

#### start_servers

参数：
 + `server_ids: Array<string>` 

返回：
 + 无

#### stop_servers

参数：
 + `server_ids: Array<string>` 

返回：
 + 无