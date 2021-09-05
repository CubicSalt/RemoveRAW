# RemoveRAW
摄影师选图脚本，用于删除 .ARW 文件，只留下与 .JPG 对应的 .ARW 格式文件

## 使用方法：
- 安装 Python 和 Git 并选择一个目录
- `git clone git@github.com:CubicSalt/RemoveRAW.git`
- `cd RemoveRAW`
- `python DeleteARW.py -p [YourPath]`

## 注意：
- 如果 ARW 文件 和 JPG 文件不在一个文件夹，使用 `python DeleteARW.py -p [YourJPGPath] -a [YourARWPath]`
- 只能根据 JPG 文件来删除多余的 ARW 文件，适用于索尼用户，其他用户请自行在代码中更改文件后缀名
- 不保证安全性，建议提前备份
