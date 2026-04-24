# MLX Experiments

```bash
mlx_vlm.server --port 8080 --model mlx-community/gemma-4-e2b-it-5bit
```

```bash
curl -X POST "http://localhost:8080/chat/completions" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "mlx-community/gemma-4-e2b-it-5bit",
    "messages": [
      {
        "role": "user",
        "content": "Hello, how are you"
      }
    ],
    "stream": true,
    "max_tokens": 100
  }'
```
