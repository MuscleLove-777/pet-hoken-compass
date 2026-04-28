"""ペット保険コンパス - ブログ固有設定"""
import os
from pathlib import Path

BASE_DIR = Path(__file__).parent

BLOG_NAME = "ペット保険コンパス"
BLOG_DESCRIPTION = "アイペット・アニコム・SBIプリズム等のペット保険を犬種・猫種・年齢別に徹底比較。補償範囲・保険料・通院/入院/手術の支払い割合まで網羅。"
BLOG_URL = "https://musclelove-777.github.io/pet-hoken-compass/"
BLOG_LANGUAGE = "ja"
GITHUB_REPO = "MuscleLove-777/pet-hoken-compass"

TARGET_CATEGORIES = [
    "ペット保険会社比較",
    "犬種別おすすめ保険",
    "猫種別おすすめ保険",
    "シニアペット向け保険",
    "病気・ケガ別対応",
    "保険金請求の流れ",
    "免責事項・告知義務",
    "保険料節約術",
]

THEME = {
    "primary": "#7b6d8d",
    "accent": "#f1a208",
    "gradient_start": "#7b6d8d",
    "gradient_end": "#f1a208",
}

GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY", "")
GEMINI_MODEL = "gemini-2.5-flash"
GEMINI_FALLBACK_MODEL = "gemini-2.5-flash-lite"

OUTPUT_DIR = BASE_DIR / "output"
ARTICLES_DIR = OUTPUT_DIR / "articles"
SITE_DIR = OUTPUT_DIR / "site"
TOPICS_DIR = OUTPUT_DIR / "topics"

MAX_ARTICLE_LENGTH = 4000
SEO_KEYWORD_DENSITY = 0.02
