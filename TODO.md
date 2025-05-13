# Day 1
1. 创建后端GitHub仓库SecondDraft_Backend

2. 使用conda创建虚拟环境sdraft-env

3. 安装核心依赖库flask, flask-cors, flask-sqlalchemy, flask-jwt-extended, python-dotenv, openai

4. 初始化Flask项目结构
   - app/：
     - __init__.py
     - routes.py
     - models.py
     - utils.py
   - 根目录：
     - run.py
     - config.py
     - .env.example
     - requirements.txt

5. 编写create_app()
   - 初始化扩展：CORS、SQLAlchemy、JWT
   - 注册Blueprint
   - 加载环境变量配置

# Day 2
1. 定义用户模型（models.py）
   - 字段：id, username, email, password_hash, created_at
   - 方法：set_password()、check_password()

2. 编写密码加密工具（utils.py）
   - 函数：hash_password(raw_password)
   - 函数：verify_password(hashed, raw_password)

3. 初始化数据库
   - 在run.py中添加 db.create_all()
   - 启动服务并验证User表是否创建成功

4. 用Redis作为临时缓存，实现登录失败次数限制+临时封锁机制
   - Redis自带TTL，可以自动过期，适合做登录节流（throttling）

5. 实现注册接口（routes.py）
   - 接收username、email、password
   - 校验重复、写入用户
   - 返回注册成功或失败消息

6. 实现登录接口（routes.py）
   - 接收email、password
   - 验证密码，生成并返回JWT access_token

7. 添加受保护接口示例（routes.py）
   - 创建/api/protected 路由
   - 验证JWT token 后返回当前用户信息

8. 使用Postman测试接口功能
   - 测试注册、登录、token 获取与验证流程
