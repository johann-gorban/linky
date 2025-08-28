import csv
import sys
import io

from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent.parent))

from database.crud import db
from database.models import LinkRecord
from typing import List, Any, Optional


async def create_csv(text: List[Any]) -> bytes:
    buffer = io.StringIO()
    writer = csv.writer(buffer)
    writer.writerows(text)

    buffer.seek(0)

    csv_bytes = buffer.getvalue().encode('utf-8')

    return csv_bytes


async def extract_all_links(user_id: Optional[str] = None) -> List[List[str]]:
    links: List[LinkRecord] = []
    if user_id is not None:
        links = await db.get_links_by_user_id(user_id)
    else:
        links = await db.get_all_links()

    return [
        [link.user_id, link.url] for link in links
    ]



async def extract_links(user_id: Optional[str] = None) -> List[List[str]]:
    links: List[LinkRecord] = []
    if user_id is not None:
        links = await db.get_links_by_user_id(user_id)
    else:
        links = await db.get_all_links()
    
    url_list = [link.url for link in links]
    
    unique_urls = list(set(url_list))
    
    return [[url] for url in unique_urls]