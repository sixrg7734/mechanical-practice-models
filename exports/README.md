# exports — 导出文件

存放从 FreeCAD 导出的交换格式文件：

| 格式 | 用途 | 导出方式 |
| --- | --- | --- |
| `.step` | 通用三维交换格式，其他 CAD 软件可直接打开 | 选中实体 → File → Export |
| `.stl` | 3D 打印切片用网格格式 | 选中实体 → File → Export |

说明：

- 命名建议与源文件一致，如 `l-bracket.step`、`l-bracket.stl`
- 导出 STL 前可在 Preferences → Part/Part Design → Mesh view 调整网格精度，精度越高文件越大
