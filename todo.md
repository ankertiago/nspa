我想开发一个类似spec-kit功能，用户安装我的代码并init，就可以在项目代码里面生成类似的文件。
specify需要选择ai平台。我的需要，直接就是claude code。
将我本地项目里面的install文件夹里面的md复制到项目仓库里面：.claude/commands 文件夹里面。


specify原来的命令是：
uv tool install specify-cli --from git+https://github.com/github/spec-kit.git
specify init <PROJECT_NAME>

我的命令是：
uv tool install nspa-cli --from git+https://github.com/ankertiago/nspa-kit.git
nspa init <PROJECT_NAME>