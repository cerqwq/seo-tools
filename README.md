# 🔍 SEO Tools

AI SEO工具集，支持SEO审计、元数据、结构化数据。

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-blue?logo=python" />
  <img src="https://img.shields.io/badge/OpenAI-API-green?logo=openai" />
  <img src="https://img.shields.io/badge/License-MIT-yellow" />
</p>

## ✨ 特性

- 📊 页面SEO审计
- 🏷️ Meta标签生成
- 📋 Schema标记生成
- 🤖 robots.txt生成
- 🗺️ Sitemap生成
- 🔑 关键词分析

## 🚀 快速开始

```bash
pip install openai

python tools.py
```

## 📖 使用

```python
from seo_tools import create_tools

tools = create_tools()

# 审计页面
audit = tools.audit_page(html, url)

# Meta标签
meta = tools.generate_meta_tags(page_info)

# Schema标记
schema = tools.generate_schema_markup("Article", data)

# robots.txt
robots = tools.generate_robots_txt(site_info)

# Sitemap
sitemap = tools.generate_sitemap(pages)

# 关键词分析
keywords = tools.analyze_keywords(content, "Python编程")
```

## 📁 项目结构

```
seo-tools/
├── tools.py       # SEO工具核心
└── README.md
```

## 📄 许可证

MIT License
