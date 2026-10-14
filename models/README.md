# models — FreeCAD 源文件

存放 FreeCAD 建模源文件（`.FCStd`），文件名与 README 零件清单保持一致：

| 文件 | 零件 |
| --- | --- |
| `l-bracket.FCStd` | L型固定支架 |
| `washer.FCStd` | 带孔垫片 |

说明：

- 源文件是仓库的主角，请保留可编辑版本，不要只提交导出的 STEP / STL
- `.FCStd1`、`.FCBak`、`.autosave` 等自动备份文件已由 `.gitignore` 排除，不会误提交
- 大体积模型文件已被 `.dshignore` 排除，避免 AI 工具读取时卡顿
