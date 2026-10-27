"""Validate WHOOP publication artifacts; no claim of clinical certification."""
from collections import Counter
from hashlib import sha256
from html import unescape
from html.parser import HTMLParser
import json
from pathlib import Path
import re

BASE=Path(__file__).resolve().parent


class Media(HTMLParser):
    def __init__(self):
        super().__init__();self.images=[]
    def handle_starttag(self,tag,attrs):
        if tag=='img':self.images.append(dict(attrs))


def main():
    articles=json.loads((BASE/'articles.json').read_text())
    records=json.loads((BASE/'data/whoop_article_records.json').read_text())
    refs={s['id']:s for s in json.loads((BASE/'data/whoop_sources.json').read_text())}
    figures=json.loads((BASE/'data/whoop_image_manifest.json').read_text())
    assert len(articles)==len({a['id'] for a in articles})==112
    assert len(records)==29
    assert {a['id'] for a in records}=={f'WHOOP-ART-{n:02d}' for n in range(1,30)}
    assert [a for a in articles if a['id'].startswith('WHOOP-ART-')]==records
    source_data=(BASE/'articles_data.js').read_text().strip()
    assert json.loads(source_data.removeprefix('const articles = ').removesuffix(';'))==articles
    for a in records:
        assert a['available_languages']==['vi'] and a['content_language']=='vi'
        assert a['independent_rewrite'] and a['published_on']=='2026-10-27'
        assert a['clinical_review_status']=='Not recorded'
        assert 'Vietnamese edition' in a['content']
        assert a['content_vi'] in a['content']
        assert len(a['content_vi'].split())>=250
        assert a['public_url']==f'https://test-repo-y1wb.onrender.com/posts/{a["id"]}.html?lang=vi'
        assert len(a['references'])>=2
        for ref in a['references']:
            source=refs[ref['id'].removeprefix('whoop_')]
            assert ref['url']==source['url'] and ref['url'] in a['content_vi']
        page=(BASE/'posts'/(a['id']+'.html')).read_text()
        assert a['title_vi'] in page and a['title'] in page
        assert 'Vietnamese edition' in page
        assert 'bản dịch nguyên văn' not in a['content_vi']
        parser=Media();parser.feed(page)
        assert len(parser.images)==4,a['id']
        for img in parser.images:
            assert img.get('alt')
            src=img['src']
            if not src.startswith(('https://','http://','data:')):
                assert (BASE/'posts'/src).resolve().is_file(),(a['id'],src)
        for role in ['hero_image','inline_image']:
            assert (BASE/a[role]).is_file()
        assert sha256((BASE/a['inline_image']).read_bytes()).hexdigest()==figures[a['id']]['sha256']
        credit=a['image_attributions'][0]
        assert sha256((BASE/credit['asset']).read_bytes()).hexdigest()==credit['sha256']
        assert credit['author'] in unescape(page) and credit['license_url'] in unescape(page)
        assert credit['role']=='hero'
        for ref in a['references']:
            assert ref['url'] in unescape(page)
    before=BASE.parent/'audit/whoop-publication-2026-10-27/before/Health_Blog_Demo/articles.json'
    if before.exists():
        assert articles[:83]==json.loads(before.read_text()),'Existing article records changed'
    print(f'PASS: 29 independent Vietnamese WHOOP articles; 112 total records; 29 standalone pages; sources, licensed heroes and original SVGs match.')


if __name__=='__main__':
    main()
