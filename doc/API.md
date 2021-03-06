接口信息
-------------
## `/user` 用户接口

### `路由`  `请求方法` `权限` 简述

### `/login`  `GET` `POST` `USER`  登录
* GET     
    返回 测试页面（不准确） 在生产环境中被弃用
    
* POST  
    获取 
    + 用户名 username  
    + 密码 password   
    
    返回 登录信息
    

### `/logout`  `GET` 登出当前用户
* GET     
    返回 登出消息


### `/detail`  `GET` 获取当前用户详细信息
* GET     
    返回 当前用户信息 UserInfo


### `/register`  `GET` `POST` 注册用户
* GET     
    返回 测试页面（不准确） 在生产环境中被弃用
    
* POST  
    获取  
    + 用户名 username 
    + 密码 password 
    + 邮箱 email
    + 手机号码 mobile  
    + 地址 location
    + 出生日期 birth 

    返回 用户信息 UserInfo


### `/update`  `GET` `POST` 更新当前用户详细信息
* GET     
    返回 测试页面（不准确） 在生产环境中被弃用
    
* POST  
    获取  
    + 邮箱 email
    + 手机号码 mobile  
    + 地址 location
    + 出生日期 birth 
    + 描述 description
    
    返回 用户信息 UserInfo  
    
* 注 这里的获取内容可以缺省


### `/new_cost`  `GET` `POST` 用户新建 COST 工单
* GET     
    返回 测试页面（不准确） 在生产环境中被弃用
    
* POST  
    获取  
    + 工单描述 remarks
    
    返回 工单信息 WorkOrder  


### `/new_earning`  `GET` `POST` 用户新建 EARNING 工单
* GET     
    返回 测试页面（不准确） 在生产环境中被弃用
    
* POST  
    获取  
    + 工单描述 remarks
    
    返回 工单信息 WorkOrder  


### `/new_comprehensive`  `GET` `POST` 用户新建 COMPREHENSIVE 工单
* GET     
    返回 测试页面（不准确） 在生产环境中被弃用
* POST  
    获取  
    + 工单描述 remarks
    + 上传（单个）数据集 csv文件 file
    
    返回 工单信息 WorkOrder  


### `/all_work_order`  `GET`  查询所用户的所有工单
* GET     
    返回 当前用户持有的所有工单 WorkOrder[]


### `/detail_work_order`  `GET` `POST` 查询工单详情
* GET     
    返回 测试页面（不准确） 在生产环境中被弃用
* POST  
    获取  
    + 工单id order_id
    
    返回 工单信息 WorkOrder 与 具体工单信息 CostValuation/EarningValuation/ComprehensiveValuation  


### `/apply_expert`  `GET` `POST` 申请专家权限



## `/expert` 专家接口

### `/login`  `GET` `POST` `USER`  登录

* GET     
    返回 测试页面（不准确） 在生产环境中被弃用
    
* POST  
    获取 用户名 username 密码 password   
    返回 登录信息


### `/logout`  `GET` 登出当前用户
* GET     
    返回 登出消息


### `/detail`  `GET` 获取当前专家详细信息
* GET     
    返回 当前专家信息 ExpertInfo


### `/update`  `GET` `POST` 更新当前用户详细信息
* GET     
    返回 测试页面（不准确） 在生产环境中被弃用
    
* POST  
    获取  
    + 邮箱 email
    + 手机号码 mobile  
    + 地址 location
    + 出生日期 birth 
    + 描述 description
    
    返回 专家信息 ExpertInfo  
    
* 注 这里的获取内容可以缺省


### `/all_wait_work_order`  `GET`  查看所有待评估的工单
* GET     
    返回 所有待评估的工单 WorkOrder[]


### `/all_self_work_order`  `GET`  查看所有自己负责的工单
* GET     
    返回 所有自己负责的工单 WorkOrder[]


### `/detail_work_order`  `GET` `POST` 查询工单详情
* GET     
    返回 测试页面（不准确） 在生产环境中被弃用
    
* POST  
    获取  
    + 工单id order_id
    
    返回 工单信息 WorkOrder 与 具体工单信息 CostValuation/EarningValuation/ComprehensiveValuation  


### `/download_order_file`  `GET` `POST` 获取某工单附件
* GET     
    返回 测试页面（不准确） 在生产环境中被弃用
    
* POST  
    获取  
    + 工单id order_id

    返回 工单附件 file  


### `/process_comprehensive`  `GET` `POST` 评估 COMPREHENSIVE 工单
* GET     
    返回 测试页面（不准确） 在生产环境中被弃用
    
* POST  
    获取  
    + 工单id order_id
    + rareness
    + timeliness  
    + dimensional
    + economy 
    + 质量权重 数组 quality_weight
    + 应用权重 数组 applied_weight
    
    返回 COMPREHENSIVE 工单信息 ComprehensivetValuation  
    

### `/process_cost`  `GET` `POST` 评估 COST 工单
* GET     
    返回 测试页面（不准确） 在生产环境中被弃用
    
* POST  
    获取  
    + 工单id order_id
    + R
    + C  
    + II
    + M 
    + E
    
    返回 COST 工单信息 CostValuation  
    

### `/process_earning`  `GET` `POST` 评估 EARNING 工单
* GET     
    返回 测试页面（不准确） 在生产环境中被弃用
    
* POST  
    获取  
    + 工单id order_id
    + n
    + r  
    + 数组 R
    
    返回 EARNING 工单信息 EarningValuation  
    



## `/admin` 管理员接口

### `/login`  `GET` `POST` `USER`  登录

* GET     
    返回 测试页面（不准确） 在生产环境中被弃用
    
* POST  
    获取 用户名 username 密码 password   
    返回 登录信息 Login


### `/logout`  `GET` 登出当前用户
* GET     
    返回 登出消息


### `/detail`  `GET` 获取当前管理员详细信息
* GET     
    返回 当前管理员信息 AdminInfo


### `/update`  `GET` `POST` 更新当前管理员详细信息
* GET     
    返回 测试页面（不准确） 在生产环境中被弃用
    
* POST  
    获取  
    + 邮箱 email
    + 手机号码 mobile  
    + 地址 location
    + 出生日期 birth 
    + 描述 description
    
    返回 管理员信息 AdminInfo
    
* 注 这里的获取内容可以缺省


### `/get_user_info`  `GET` `POST` 查询用户信息
* GET     
    返回 所有用户信息 UserInfo[]
    
* POST  
    获取  
    + 用户id id
    + 用户名 username  
    + 邮箱 email
    + 地址 location
    
    返回 用户信息 UserInfo[]
    
* 注 这里的获取内容可以缺省


### `/update_user_info`  `POST` 更新某用户信息
* POST  
    获取  
    + 用户id id
    + 邮箱 email
    + 手机号码 mobile  
    + 地址 location
    + 出生日期 birth 
    + 描述 description
    
    返回 用户信息 UserInfo
    
* 注 这里的获取内容可以缺省


### `/get_work_order`  `GET` `POST` 查询工单信息
* GET     
    返回 所有工单信息 WorkOrder[]
    
* POST  
    获取  
    + 工单id order_id
    
    返回 工单信息 WorkOrder[]
    
* 注 这里的获取内容可以缺省


### `/get_login_log`  `GET` `POST` 查询登录日志信息
* GET     
    返回 所有登录日志信息 LoginLog[]
    
* POST  
    获取  
    + 用户名 username
    
    返回 登录日志信息 LoginLog[]
    
* 注 这里的获取内容可以缺省


### `/get_log`  `GET` `POST` 查询日志信息
* GET     
    返回 所有工单信息 Log[]
    
* POST  
    获取  
    + 用户名 username
    
    返回 日志信息 Log[]
    
* 注 这里的获取内容可以缺省

    
