# 01-概念约定 目录说明

本目录用于统一“业务知识网络”的概念层（TBox）资料，涵盖示例数据、规范与校验文件，确保跨团队协作时结构清晰、无歧义。

## 文件总览
- `术语约定.md`
  - 作用：术语定义与边界说明（TBox/ABox、对象类/对象实例、关系类等），确保口径统一。
- `kn_tbox.json`
  - 作用：最小化示例 TBox 文档，面向当前需求（从 TBox 中找到与 query 相关的对象类与关系类）。
  - 结构：
    - `network_info`：`id`、`network_name`（可选 `comment/object_types_count/relation_types_count`）。
    - `object_types[]`：`id`、`name`、`tags?`、`comment?`、`data_properties[]`（属性含 `name`、`display_name?`、`type?`、`comment?`）。
    - `relation_types[]`：`id`、`name`、`tags?`、`comment?`、`source_object_type{id,name}`、`target_object_type{id,name}`。

- `kn_tbox_example.json`
  - 作用：补充示例（可用于对照或扩展），结构与 `kn_tbox.json` 一致或略有增强。

- `kn_tbox.openapi.yaml`
  - 作用：OpenAPI 3.0 Schema，按照 `kn_tbox.json` 的结构定义 TBox 文档模型（仅组件，无接口）。
  - 用法：用于在 OpenAPI 工具（Swagger/Stoplight/Apidog 等）中统一模型口径，或作为跨服务/语言的契约源。