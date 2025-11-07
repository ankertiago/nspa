如何更新脚本呢？
- 这是安装
uv tool install nspa-cli --from git+https://github.com/ankertiago/nspa.git
- 更新：
uv tool update nspa-cli --from git+https://github.com/ankertiago/nspa.git
- 如果 uv 版本较老，可以用强制重装：
uv tool install nspa-cli --from git+https://github.com/ankertiago/nspa.git --reinstall
