from datetime import datetime
from typing import Optional
from re import sub
import re

from .models.hors_parse_result import HorsParseResult
from .hors_text_parser import parse


def preprocess(phrase: str) -> str:
    phrase = sub(r'(\d{1,2})(am|pm)', r"\1 \2", phrase)
    phrase = sub(r'\bin the\b', '', phrase, flags=re.IGNORECASE)
    phrase = sub(r'\bin a\b', 'in', phrase, flags=re.IGNORECASE)
    phrase = sub(r'half an hour', '30 minutes', phrase, flags=re.IGNORECASE)
    phrase = sub(r'an hour and a half', '1 hour 30 minutes', phrase, flags=re.IGNORECASE)
    phrase = sub(r'couple of hours', '2 hours', phrase, flags=re.IGNORECASE)
    phrase = sub(r'at noon', 'at 12:00 PM', phrase, flags=re.IGNORECASE)
    phrase = sub(r'\bafter noon\b|\bafternoon\b', 'at 3:00 PM', phrase, flags=re.IGNORECASE)
    phrase = sub(r'the day after tomorrow', 'послезавтра', phrase, flags=re.IGNORECASE)
    phrase = sub(r'day after tomorrow', 'послезавтра', phrase, flags=re.IGNORECASE)
    phrase = sub(r'\b(?:a\.m\.?|p\.m\.?)\b', lambda m: m.group().replace('.', '').lower(), phrase, flags=re.IGNORECASE)


    # swap syntax
    phrase = sub(r'after (\d+) (minutes|hours|day)', r'in \1 \2', phrase, flags=re.IGNORECASE)
    phrase = sub(r'(\d+) (minutes|hours|day) later', r'in \1 \2', phrase, flags=re.IGNORECASE)
    pattern = r"\b(jan(?:uary)?|feb(?:ruary)?|mar(?:ch)?|apr(?:il)?|may|jun(?:e)?|jul(?:y)?|aug(?:ust)?|sep(?:tember)?|oct(?:ober)?|nov(?:ember)?|dec(?:ember)?)\b ([1-9]|[1-9][0-9])\b"

    phrase = sub(pattern, r"\2 \1", phrase, flags=re.IGNORECASE)
    phrase = sub(r'(\d+) and a half hours', r'\1 hours 30 minutes', phrase, flags=re.IGNORECASE)

    # change forms
    phrase = sub(r'часок', 'час', phrase, flags=re.IGNORECASE)
    phrase = sub(r'часиков', 'часов', phrase, flags=re.IGNORECASE)
    phrase = sub(r'минуток', 'минут', phrase, flags=re.IGNORECASE)

    # translate times
    phrase = sub(r'полчаса', '30 минут', phrase, flags=re.IGNORECASE)
    phrase = sub(r'полчасика', '30 минут', phrase, flags=re.IGNORECASE)
    phrase = sub(r'полтора часа', '1 час 30 минут', phrase, flags=re.IGNORECASE)
    phrase = sub(r'через пару часов', 'через 2 часа', phrase, flags=re.IGNORECASE)
    phrase = sub(r'в обед', 'в 13 часов', phrase, flags=re.IGNORECASE)
    phrase = sub(r'после обеда', 'в 14 часов', phrase, flags=re.IGNORECASE)

    # swap syntax
    phrase = sub(r'через (минут|часов|часа) (\d*)', r'через \2 \1', phrase, flags=re.IGNORECASE)
    phrase = sub(r'(минут|часов|часа) через (\d*)', r'через \2 \1', phrase, flags=re.IGNORECASE)
    phrase = sub(r'в течение (\w*а)', r'через \1', phrase, flags=re.IGNORECASE)
    phrase = sub(r'получас', '30 минут', phrase, flags=re.IGNORECASE)
    phrase = sub(r'(\d+) с половиной часа', r'\1 часа 30 минут', phrase, flags=re.IGNORECASE)
    return phrase


def preprocess_today(phrase: str) -> str:
    phrase = re.sub(r'вечерком', 'вечером', phrase, flags=re.IGNORECASE)
    phrase = re.sub(r'ближе к вечеру', 'вечером', phrase, flags=re.IGNORECASE)
    phrase = sub(r'(вечером|днём|утром|evening|noon|morning)', r'сегодня \1', phrase, flags=re.IGNORECASE)
    return phrase


def process_phrase(phrase: str, now: Optional[datetime] = None) -> HorsParseResult:
    phrase = preprocess(phrase)
    now = now or datetime.now()
    hors_result = parse(phrase, now)
    if not hors_result.dates:
        phrase = preprocess_today(phrase)
        hors_result = parse(phrase, now)

    return hors_result
