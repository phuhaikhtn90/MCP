# Hướng dẫn sử dụng Figma API Extractor

## Cài đặt

1. **Cài đặt dependencies:**
```bash
cd figma_mcp/get_figma_api_restructured
pip install -r requirements.txt
```

2. **Cấu hình API:**
```bash
# Copy file cấu hình
cp config/.env.example config/.env

# Chỉnh sửa file .env với thông tin thực tế
nano config/.env
```

Thêm thông tin Figma API của bạn:
```
FIGMA_TOKEN=your_actual_figma_token_here
FIGMA_FILE_KEY=your_actual_figma_file_key_here
```

## Sử dụng

### 1. Sử dụng script có sẵn

```bash
# Chạy script extract tất cả dữ liệu
python3 scripts/extract_all.py
```

### 2. Sử dụng trong code Python

```python
from figma_extractor import FigmaExtractor

# Khởi tạo extractor
extractor = FigmaExtractor()

# Hoặc với token và file key cụ thể
extractor = FigmaExtractor(
    token="your_token", 
    file_key="your_file_key"
)

# Extract design tokens
tokens = extractor.extract_tokens()

# Extract frames
frames = extractor.extract_frames()

# Extract components với node ID cụ thể
components = extractor.extract_components("2-96")

# Tính toán khoảng cách
distances = extractor.calculate_distances(tokens)

# Làm sạch dữ liệu
clean_data = extractor.clean_data(tokens)
```

### 3. Sử dụng từng module riêng lẻ

```python
from figma_extractor.core.api_client import FigmaAPIClient
from figma_extractor.extractors.frame_extractor import FrameExtractor

# Tạo API client
client = FigmaAPIClient(token="your_token", file_key="your_file_key")

# Sử dụng frame extractor
frame_extractor = FrameExtractor(client)
frames = frame_extractor.extract()
```

## Cấu trúc dữ liệu đầu ra

### Frames
```json
{
  "id": "frame_id",
  "name": "Frame Name",
  "x": 0,
  "y": 0,
  "width": 100,
  "height": 100,
  "child_count": 5
}
```

### Components (đã làm sạch)
```json
{
  "id": "component_id",
  "name": "Component Name",
  "type": "FRAME",
  "absoluteBoundingBox": {...},
  "padding": {
    "left": 10,
    "top": 10,
    "right": 10,
    "bottom": 10
  },
  "siblingsLayout": [
    {
      "targetId": "sibling_id",
      "relation": "sameRow",
      "distance": 20
    }
  ]
}
```

## Chạy tests

```bash
# Chạy tất cả tests
python3 -m pytest tests/

# Chạy test cụ thể
python3 -m pytest tests/test_extractors.py

# Hoặc sử dụng unittest
python3 -m unittest tests.test_extractors
```

## Cấu trúc thư mục

```
figma_api_extractor/
├── src/figma_extractor/     # Source code chính
├── tests/                   # Unit tests
├── data/                    # Dữ liệu input/output
├── config/                  # File cấu hình
├── scripts/                 # Scripts tiện ích
└── docs/                    # Documentation
```

## Lưu ý

- Đảm bảo có token Figma API hợp lệ
- File key phải là key của file Figma bạn muốn truy cập
- Dữ liệu sẽ được lưu trong thư mục `data/output/`
- Logs sẽ hiển thị quá trình xử lý

## Troubleshooting

### Lỗi 403 Forbidden
- Kiểm tra token Figma API có đúng không
- Đảm bảo có quyền truy cập file Figma

### Lỗi import module
- Kiểm tra đã cài đặt dependencies chưa
- Đảm bảo đang chạy từ thư mục gốc của project

### Lỗi file không tìm thấy
- Kiểm tra file key có đúng không
- Đảm bảo file Figma tồn tại và có thể truy cập
