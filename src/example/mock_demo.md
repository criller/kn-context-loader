# 企业经营健康度 Mock API 演示

已成功创建并验证了企业经营健康度 Mock 接口。

## 成果产物

1.  **OpenAPI 定义**: [api/business_health_mock.yaml](../../../api/business_health_mock.yaml)
2.  **Mock 服务器脚本**: [mock_health_server.py](./mock_health_server.py)

## 验证结果

启动服务器后，对不同公司 ID 进行了测试，返回结果符合预期。

**命令**:
```bash
python3 mock_health_server.py
```

**测试案例 A (低分)**: `company_test_A`
```json
{
  "company_id": "company_test_A",
  "overall_score": 56,
  "rating": "D",
  "suggestion": "企业经营风险较高，建议谨慎合作或进行合规整改。",
  "dimensions": {
    "scale_score": 49,
    "innovation_score": 52,
    "compliance_score": 58,
    "stability_score": 64
  }
}
```

**测试案例 B (高分)**: `company_test_B`
```json
{
  "company_id": "company_test_B",
  "overall_score": 81,
  "rating": "A",
  "suggestion": "企业综合实力强劲，建议关注细分领域的创新机会。",
  "dimensions": {
    "scale_score": 82,
    "innovation_score": 76,
    "compliance_score": 76,
    "stability_score": 87
  }
}
```

## 如何运行

1.  在终端中执行：
    ```bash
    cd src/example
    python3 mock_health_server.py
    ```
2.  访问接口：
    ```
    http://localhost:8080/api/v1/company/{任意公司ID}/health-score
    ```
