"""
SEO Tools - AI SEO工具集
支持SEO审计、元数据、结构化数据
"""

import json
import os
from typing import Dict, List, Any
from datetime import datetime

try:
    from openai import OpenAI
    OPENAI_AVAILABLE = True
except ImportError:
    OPENAI_AVAILABLE = False


class SEOTools:
    """
    AI SEO工具集
    支持：审计、元数据、结构化数据
    """

    def __init__(self, model: str = "mimo-v2.5-pro", api_key: str = None, base_url: str = None):
        self.model = model
        if OPENAI_AVAILABLE:
            self.client = OpenAI(
                api_key=api_key or os.environ.get('OPENAI_API_KEY', ''),
                base_url=base_url or os.environ.get('OPENAI_BASE_URL', 'https://api.xiaomimimo.com/v1')
            )
        else:
            self.client = None

    def audit_page(self, html: str, url: str = "") -> Dict:
        """审计页面SEO"""
        if not self.client:
            return {"error": "LLM客户端未配置"}

        prompt = f"""请审计以下页面的SEO：

URL：{url}
HTML：
{html[:2000]}

请返回JSON格式：
{{
    "score": 1-100,
    "issues": [
        {{"type": "error/warning/info", "category": "类别", "description": "描述", "fix": "修复建议"}}
    ],
    "meta_tags": {{}},
    "headings": {{}},
    "images": {{}}
}}"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=1000
        )

        try:
            content = response.choices[0].message.content
            import re
            json_match = re.search(r'\{.*\}', content, re.DOTALL)
            if json_match:
                return json.loads(json_match.group())
        except:
            pass

        return {"audit": content}

    def generate_meta_tags(self, page_info: Dict) -> str:
        """生成Meta标签"""
        if not self.client:
            return "LLM客户端未配置"

        info_text = json.dumps(page_info, ensure_ascii=False)

        prompt = f"""请根据以下页面信息生成Meta标签：

{info_text}

请返回完整的HTML meta标签："""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=500
        )

        return response.choices[0].message.content

    def generate_schema_markup(self, page_type: str, data: Dict) -> str:
        """生成Schema标记"""
        if not self.client:
            return "LLM客户端未配置"

        data_text = json.dumps(data, ensure_ascii=False)

        prompt = f"""请为{page_type}页面生成Schema.org JSON-LD：

{data_text}

请返回完整的JSON-LD代码："""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=1000
        )

        return response.choices[0].message.content

    def generate_robots_txt(self, site_info: Dict) -> str:
        """生成robots.txt"""
        if not self.client:
            return "LLM客户端未配置"

        info_text = json.dumps(site_info, ensure_ascii=False)

        prompt = f"""请根据以下站点信息生成robots.txt：

{info_text}

请返回完整的robots.txt内容："""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=500
        )

        return response.choices[0].message.content

    def generate_sitemap(self, pages: List[Dict]) -> str:
        """生成Sitemap"""
        if not self.client:
            return "LLM客户端未配置"

        pages_text = json.dumps(pages, ensure_ascii=False)

        prompt = f"""请根据以下页面生成XML Sitemap：

{pages_text}

请返回完整的XML格式Sitemap："""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=2000
        )

        return response.choices[0].message.content

    def analyze_keywords(self, content: str, topic: str) -> Dict:
        """分析关键词"""
        if not self.client:
            return {"error": "LLM客户端未配置"}

        prompt = f"""请分析以下内容的关键词：

主题：{topic}
内容：{content[:1000]}

请返回JSON格式：
{{
    "primary_keyword": "主关键词",
    "secondary_keywords": ["次关键词"],
    "keyword_density": "关键词密度",
    "suggestions": ["优化建议"]
}}"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=500
        )

        try:
            content = response.choices[0].message.content
            import re
            json_match = re.search(r'\{.*\}', content, re.DOTALL)
            if json_match:
                return json.loads(json_match.group())
        except:
            pass

        return {"keywords": content}


def create_tools(**kwargs) -> SEOTools:
    """创建SEO工具"""
    return SEOTools(**kwargs)


if __name__ == "__main__":
    tools = create_tools()

    print("SEO Tools")
    print()

    # 测试
    meta = tools.generate_meta_tags({
        "title": "Python教程",
        "description": "学习Python编程",
        "url": "https://example.com/python"
    })
    print(meta)
