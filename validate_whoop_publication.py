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
        super().__init__();self.images=[];self.visible=[];self.skip=0
    def handle_starttag(self,tag,attrs):
        if tag in ['script','style']:self.skip+=1
        if tag=='img':self.images.append(dict(attrs))
        assert tag.lower() not in ['tên','ten'],'App placeholder became an HTML element'
    def handle_endtag(self,tag):
        if tag in ['script','style']:self.skip-=1
    def handle_data(self,data):
        if not self.skip:self.visible.append(data)


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
        assert a['title_vi'] in unescape(page) and a['title'] in unescape(page)
        assert 'Vietnamese edition' in page
        assert 'bản dịch nguyên văn' not in a['content_vi']
        parser=Media();parser.feed(page)
        assert len(parser.images)==(2 if a['hero_image'] else 0),a['id']
        visible=' '.join(parser.visible)
        assert not re.search('WHOOP',visible,re.I),(a['id'],'Brand still visible in article')
        assert '<Tên App/>' in visible,(a['id'],'Literal app placeholder missing')
        assert not a['inline_image'] and 'article-inline-diagram' not in page
        assert a['reader_revision']==3 and a['visual_policy']=='prose_first_no_text_card_diagram'
        for img in parser.images:
            assert img.get('alt')
            src=img['src']
            if not src.startswith(('https://','http://','data:')):
                assert (BASE/'posts'/src).resolve().is_file(),(a['id'],src)
        assert figures[a['id']]['active'] is False
        if a['hero_image']:
            assert (BASE/a['hero_image']).is_file()
            credit=a['image_attributions'][0]
            assert sha256((BASE/credit['asset']).read_bytes()).hexdigest()==credit['sha256']
            assert credit['author'] in unescape(page) and credit['license_url'] in unescape(page)
            assert credit['role']=='hero'
        else:assert not a['image_attributions']
        for ref in a['references']:
            assert ref['url'] in unescape(page)
    before=BASE.parent/'audit/whoop-publication-2026-10-27/before/Health_Blog_Demo/articles.json'
    if before.exists():
        assert articles[:83]==json.loads(before.read_text()),'Existing article records changed'
    previous=BASE.parent/'audit/app-content-revision-2026-10-27/before/Health_Blog_Demo/data/whoop_article_records.json'
    if previous.exists():
        for old,new in zip(json.loads(previous.read_text()),records):
            assert old['id']==new['id'] and old['public_url']==new['public_url']
            assert [r['url'] for r in old['references']]==[r['url'] for r in new['references']],(new['id'],'Reference URLs changed')
    print('PASS: 29 revised articles; literal app placeholder; no visible WHOOP branding; source URLs preserved; no text-card diagrams; optional licensed images; 83 existing records preserved.')


if __name__=='__main__':
    main()
