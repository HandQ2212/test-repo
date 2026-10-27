"""Publish the independently written WHOOP education collection into the blog data.

The portable data/whoop_article_records.json snapshot is kept in this repository.
Only --import-research reads the sibling research directory. Normal rebuilds retain
the snapshot and merge it after the 83 existing long-form records.
"""
from copy import deepcopy
from hashlib import sha256
from pathlib import Path
import argparse
import json
import math
import re
import shutil
from html import escape

BASE = Path(__file__).resolve().parent
LIVE = 'https://test-repo-y1wb.onrender.com'
PUBLISHED_ON = '2026-10-27'
PREFIX = 'WHOOP-ART-'

# Reuse reviewed, licensed assets by their actual visible subject. No WHOOP
# marketing images or screenshots are copied. Each reused image retains its credit.
HERO = {
    1: ('DM_AC_02','hero'), 3: ('DM_RC_02','hero'), 6: ('MW_NUT_01','hero'),
    9: ('LM_RC_01','inline'), 13: ('LM_SL_02','hero'), 18: ('MW_NUT_07','hero'),
    19: ('MW_NUT_03','hero'), 23: ('DM_HW_01','hero'), 26: ('DM_WH_01','hero'),
    27: ('LM_HW_02','hero'), 29: ('MW_SXH_02','hero'),
}

TAKEAWAYS = [
    'Đọc Strain cùng kế hoạch tập, Recovery và cảm nhận; không cộng điểm hai buổi theo số học.',
    'Đeo ổn định ở cổ tay và kiểm tra thời gian thiếu dữ liệu trước khi so số bước giữa các ngày.',
    'Bắt đầu từ mức vận động đang duy trì được, rồi thêm những quãng đi bộ phù hợp.',
    'Xác nhận đang dùng %HRR hay %HRmax trước khi so ngưỡng vùng giữa hai thiết bị.',
    'Kiểm tra tín hiệu và nguồn HRmax trước khi sửa; ghi lại ngày và giá trị đã thay đổi.',
    'Dùng ước tính calo để nhìn xu hướng, không điều chỉnh bữa ăn theo đúng từng calo hiển thị.',
    'Cập nhật hồ sơ và kiểm tra cách đeo trước khi diễn giải chênh lệch tiêu hao năng lượng.',
    'Đặt điểm phục hồi cạnh cảm nhận và triệu chứng trước khi chọn mức tập hôm nay.',
    'So HRV với lịch sử của chính bạn, cùng cách đo, thay vì chạy theo số của người khác.',
    'Theo dõi thay đổi nhịp thở trong cùng bối cảnh; không dùng một ngưỡng để tự chẩn đoán.',
    'Ghi thời điểm, điều kiện và triệu chứng khi đếm nhịp thở; không coi một phút ban ngày là hiệu chuẩn cho cả đêm.',
    'Ưu tiên tình trạng hiện tại khi nhịp thở tăng; khó thở rõ cần được đánh giá, không chờ thêm dữ liệu.',
    'Xem cả bốn phần điểm ngủ và cảm giác tỉnh táo để chọn thay đổi phù hợp.',
    'Phân biệt lịch ngủ đều với thời gian trên giường và thời gian thực sự ngủ.',
    'Dành cơ hội ngủ phù hợp trong những ngày tiếp theo, không chỉ chờ nợ ngủ của ứng dụng về 0.',
    'Đọc số giờ và tỷ lệ REM/SWS cùng nhau; tỷ lệ cao hơn không tự bảo đảm ngủ tốt hơn.',
    'Kiểm tra nguồn, đơn vị và điều kiện đo khối nạc; khối nạc không đồng nghĩa khối cơ.',
    'Chọn một thói quen vừa sức và có thể lặp lại, thay vì tìm sáu mẹo bảo đảm giảm cân.',
    'Ưu tiên đủ năng lượng và chất dinh dưỡng trước khi tối ưu tỷ lệ macros từ một điểm Recovery.',
    'Đọc điểm stress sinh lý cùng nhật ký cảm nhận; không dùng điểm để xác định cảm xúc hay bệnh lý.',
    'Thử một thay đổi buổi tối có thể duy trì và theo dõi cả giấc ngủ lẫn cảm nhận ban ngày.',
    'Quan tâm cảm xúc, biểu hiện cơ thể và ảnh hưởng sinh hoạt cùng với dữ liệu thiết bị.',
    'Chọn một tình huống stress thường lặp lại và đánh giá việc nghỉ/thư giãn bằng trải nghiệm thực tế.',
    'Tách nhu cầu ngủ, giờ nằm và giờ ngủ; kiểm tra cách mô hình xử lý ngủ trưa thay vì tự trừ nợ ngủ.',
    'Phân biệt Live HR với dữ liệu qua đêm; khoảng tham chiếu không thay đánh giá triệu chứng.',
    'Kiểm tra bài tập đủ điều kiện, quy ước nhập tạ và mức gắng sức trước khi so tải cơ giữa các buổi.',
    'Đọc tuổi và Pace như đầu ra mô hình; không coi đây là tuổi cơ quan hoặc dự báo tuổi thọ.',
    'Phân biệt ECG chủ động với sàng lọc IHRN; kết quả bình thường không loại trừ mọi bệnh tim.',
    'Đọc BPI như khoảng ước tính đêm, thực hiện hiệu chuẩn theo hướng dẫn và không dùng để đổi thuốc.',
]


def read(path):
    return json.loads(path.read_text(encoding='utf-8'))


def save(path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')


def cite(text, sources):
    text=text.replace('<Tên App/>','&lt;Tên App/&gt;')
    return re.sub(r'\[(S\d+)\]', lambda m: f'[{m[1]}]({sources[m[1]]["url"]})', text)


def import_research(research):
    items = read(research/'articles.json')
    sources = {s['id']:s for s in read(research/'sources.json')}
    source_labels = read(research/'public_source_labels.json')
    reviewed_images = {x['id']:x for x in read(research/'images/image_manifest.json')}
    legacy = {a['id']:a for a in read(BASE/'articles.json') if not a['id'].startswith(PREFIX)}
    assert len(items)==29 and len(legacy)==83
    records=[]
    for n,item in enumerate(items,1):
        aid=item['id']
        ref_list=[]
        for sid in item['sources']:
            s=sources[sid]
            ref_list.append(dict(id='whoop_'+sid,title=s['title'],url=s['url'],kind=s['kind'],
                                 display_label_vi=source_labels[sid],
                                 support_vi=s['supports'],support_en=s['supports'],
                                 checked_date=s['checked_on'],verification_method=s['verification_method'],
                                 publisher=s['publisher'],pmid=s.get('pmid',''),doi=s.get('doi','')))
        body=cite(item['body'],sources)
        body+='\n\n## Nguồn tham khảo và phạm vi hỗ trợ\n\n'
        for sid in item['sources']:
            s=sources[sid]
            bibliography=s.get('bibliographic_citation','')
            ids=(' PMID '+s['pmid']+'.') if s.get('pmid') else ''
            ids+=(' DOI '+s['doi']+'.') if s.get('doi') else ''
            scope=re.sub('WHOOP','thiết bị trong nguồn',s['supports'],flags=re.I)
            body+=f'- **{sid}** — {bibliography} [{source_labels[sid]}]({s["url"]}).{ids} Phạm vi tài liệu: {scope}\n'
            if s.get('related_correction'):
                r=s['related_correction']
                body+=f'  Có [đính chính liên quan]({r["url"]}); chưa đối chiếu được toàn văn đính chính.\n'
        body+=(f'\n> Bài biên soạn độc lập bởi Pulse & Vitality. Nội dung chỉnh ngày 27/10/2026; '
               f'nguồn đối chiếu {item["checked_on"]}. Liên kết được đặt tên theo chủ đề; tên tài liệu gốc và đơn vị phát hành có trên trang nguồn.\n')
        hero={}
        if n in HERO:
            source_art,role=HERO[n]
            hero=deepcopy(next(x for x in legacy[source_art]['image_attributions'] if x['role']==role))
            hero.update(article_id=aid,role='hero')
        # Captions are factual descriptions of the same, unmodified source asset.
        if n==1:
            hero.update(caption_vi='Một khoảng nghỉ giữa các hoạt động tập luyện; phân bố tải bao gồm cả lúc vận động và lúc nghỉ.',
                        caption_en='A break between exercise activities; planning load includes movement and rest.')
        elif n==6:
            hero.update(caption_vi='Bữa ăn gồm thịt gà, khoai tây và rau; ảnh minh họa, không cung cấp số calo của khẩu phần.',
                        caption_en='A meal with chicken, potatoes and vegetables; the image does not establish its calorie content.')
        elif n==18:
            hero.update(caption_vi='Các phần ăn được chuẩn bị sẵn: một ví dụ sắp xếp môi trường để bữa ăn thuận tiện hơn; không quy định khẩu phần cá nhân.',
                        caption_en='Prepared meals illustrate making food easier to access; the photo does not prescribe individual portions.')
        elif n==26:
            hero.update(caption_vi='Một người tập với tạ tay; ảnh không xác định mức tải cơ hoặc kỹ thuật phù hợp cho từng người.',
                        caption_en='A person exercising with dumbbells; the image does not establish muscular load or individualized technique.')
        elif n==29:
            hero.update(caption_vi='Đo huyết áp với vòng bít trong một buổi chăm sóc sức khỏe; ảnh minh họa phương pháp đo, không phải một ước tính từ app.',
                        caption_en='Blood pressure measurement with a cuff during health care; not an app-derived estimate.')
        if hero:
            for lang in ['vi','en']:
                hero['alt_'+lang]=hero['caption_'+lang]
        category={'Recovery_Stress':'Recovery','Life_Heart_BP':'Health & Wellness',
                  'Healthspan_Body':'Health & Wellness'}.get(item['group'],item['group'])
        limitation='Điểm số và ước tính của thiết bị cần được đọc đúng bối cảnh; bài viết không xác nhận khả năng chẩn đoán hoặc điều trị.'
        if n in (28,29):
            limitation='Khả dụng tùy thiết bị, gói và khu vực; phân biệt phạm vi ECG, IHRN và BPI. Không dùng dữ liệu để tự chẩn đoán hoặc đổi thuốc.'
        # No English translation is claimed. English UI explicitly identifies the
        # Vietnamese edition before presenting its actual Vietnamese text.
        en_body='> **Vietnamese edition:** This article is currently available in Vietnamese. The English heading is an editorial title, not a full English translation.\n\n'+body
        records.append(dict(id=aid,type='Learn more',category=category,sub_topic={'Sleep':'Giấc ngủ','Activity':'Vận động','Recovery_Stress':'Phục hồi và stress','Life_Heart_BP':'Tim mạch và huyết áp','Healthspan_Body':'Chỉ số sức khỏe dài hạn'}.get(item['group'],category),
                            gender='All',screen=category+' Screen',metric={'Activity':'Hiểu vận động', 'Sleep':'Hiểu giấc ngủ', 'Recovery_Stress':'Hiểu phục hồi và stress', 'Life_Heart_BP':'Hiểu dữ liệu tim mạch', 'Healthspan_Body':'Hiểu chỉ số sức khỏe'}.get(item['group'],'Kiến thức sức khỏe'),
                            trigger='Educational reading on wearable metrics',title=item['title_en'],title_vi=item['title_vi'],
                            description='Vietnamese edition: '+item['title_en']+'.',description_vi=item['summary_vi'],
                            content=en_body,content_vi=body,takeaway='Vietnamese edition. '+item['title_en']+'.',
                            takeaway_vi=TAKEAWAYS[n-1],reading_time=item['read_time'],reading_time_vi=item['read_time'],
                            thumbnail=hero.get('asset',''),hero_image=hero.get('asset',''),hero_image_fit=hero.get('fit','cover'),
                            hero_image_source_url=hero.get('source_page',''),hero_caption=hero.get('caption_en',''),hero_caption_vi=hero.get('caption_vi',''),
                            inline_image='',inline_image_source_url='',inline_caption='',inline_caption_vi='',
                            source_name=source_labels[item['sources'][0]],source_url=ref_list[0]['url'],references=ref_list,
                            source_checked_date=item['checked_on'],published_on=PUBLISHED_ON,
                            editorial_review_status='Independent Vietnamese rewrite; sources and limitations checked',
                            clinical_review_status='Not recorded',available_languages=['vi'],content_language='vi',
                            evidence_limitations_vi=limitation,
                            evidence_limitations_en='Device estimates require context. This Vietnamese education article does not establish diagnostic or treatment capability.',
                            image_attributions=[hero] if hero else [],image_provenance='Selected licensed illustration only where useful; text-card diagrams replaced with prose and tables.',
                            image_review_status='Subject-specific media retained with credits; no decorative text-card diagrams',
                            independent_rewrite=True,collection='App Health Education',research_content_id=aid,
                            reader_revision=3,reader_revision_date='2026-10-27',visual_policy='prose_first_no_text_card_diagram',
                            research_body_sha256=sha256(item['body'].encode()).hexdigest(),
                            original_whoop_card_title=item.get('original_title',''),
                            original_whoop_source_match=item.get('source_match',''),
                            public_url=f'{LIVE}/posts/{aid}.html?lang=vi',
                            deep_review_round=item.get('review_round',1)))
    save(BASE/'data/whoop_article_records.json',records)
    save(BASE/'data/whoop_sources.json',list(sources.values()))
    save(BASE/'data/whoop_image_manifest.json',reviewed_images)
    return records


def merge_whoop_articles():
    path=BASE/'data/whoop_article_records.json'
    if not path.exists():
        return []
    records=read(path)
    current=read(BASE/'articles.json')
    legacy=[a for a in current if not a['id'].startswith(PREFIX)]
    assert len(legacy)==83 and len(records)==29
    merged=legacy+records
    assert len({a['id'] for a in merged})==112
    save(BASE/'articles.json',merged)
    (BASE/'articles_data.js').write_text('const articles = '+json.dumps(merged,ensure_ascii=False,indent=2)+';\n',encoding='utf-8')
    manifest=read(BASE/'images/image_manifest.json')
    for a in records:
        manifest[a['id']]=dict(hero_local=a['hero_image'],figure_local=a['inline_image'],
                              hero_source_page=a['hero_image_source_url'],figure_source_page=a['inline_image_source_url'],
                              image_attributions=a['image_attributions'],creator='See asset credits; original SVG by Pulse & Vitality',
                              provenance=a['image_provenance'],evidence_urls=[r['url'] for r in a['references']])
        md=BASE/'markdown'/f'{a["id"]}.md'
        md.write_text(f'# {escape(a["title_vi"])}\n\n{a["content_vi"]}',encoding='utf-8')
    save(BASE/'images/image_manifest.json',manifest)
    return records


if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--import-research',type=Path)
    args=parser.parse_args()
    if args.import_research:
        import_research(args.import_research.resolve())
    records=merge_whoop_articles()
    print(f'WHOOP collection merged: {len(records)} original Vietnamese articles; 112 total blog records.')
