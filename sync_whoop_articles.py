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
    1: ('DM_AC_02', 'hero'),
    2: ('LM_AC_01', 'inline'),
    3: ('DM_RC_02', 'hero'),
    4: ('DM_AC_01', 'hero'),
    5: ('DM_AC_01', 'inline'),
    6: ('MW_NUT_01', 'hero'),
    7: ('DM_AC_02', 'inline'),
    8: ('DM_RC_02', 'inline'),
    10: ('DM_HW_01', 'inline'),
    11: ('DM_RC_01', 'inline'),
    12: ('MW_SXH_08', 'hero'),
    13: ('LM_SL_02', 'hero'),
    14: ('DM_SL_02', 'inline'),
    15: ('DM_SL_02', 'hero'),
    17: ('WH_30', 'inline'),
    18: ('MW_NUT_07', 'hero'),
    19: ('MW_NUT_03', 'hero'),
    20: ('LM_SL_01', 'hero'),
    21: ('MW_REL_08', 'hero'),
    22: ('MW_SXO_01', 'hero'),
    23: ('DM_HW_01', 'hero'),
    24: ('DM_SL_01', 'hero'),
    25: ('WH_16', 'hero'),
    26: ('DM_WH_01', 'hero'),
    27: ('LM_HW_02', 'hero'),
    29: ('MW_SXH_02', 'hero'),
}

HERO_CAPTIONS = {
    1: ('Người tập ngồi nghỉ sau vận động.',
        'A break between exercise activities; planning load includes movement and rest.'),
    2: ('Đi bộ nhanh ngoài trời; một hình thức vận động cơ bản để tích lũy số bước chân hàng ngày.',
        'Brisk walking outdoors; a fundamental activity for accumulating daily steps.'),
    3: ('Hai người đi bộ trên lối đi trong công viên; tạo thói quen đi bộ duy trì đều đặn mỗi ngày.',
        'Two people walking in a park; building a sustainable daily walking habit.'),
    4: ('Chạy cùng người đồng hành tạo cơ hội kiểm tra khả năng trò chuyện và duy trì đúng vùng nhịp tim.',
        'Running with a partner enables the talk test to help maintain target heart rate zones.'),
    5: ('Dây đeo ngực dùng để ghi nhận nhịp tim khi vận động.',
        'A chest strap used to record heart rate during activity.'),
    6: ('Bữa ăn gồm thịt gà, khoai tây và rau; ảnh minh họa, không cung cấp số calo của khẩu phần.',
        'A meal with chicken, potatoes and vegetables; the image does not establish its calorie content.'),
    7: ('Bữa ăn cân bằng kết hợp với vận động giúp điều hòa năng lượng nạp vào và tiêu hao trong ngày.',
        'A balanced meal alongside physical activity helps regulate daily energy intake and expenditure.'),
    8: ('Đạp xe nhẹ nhàng hoặc vận động nhẹ giúp cơ thể phục hồi chủ động sau các ngày tập nặng.',
        'Gentle cycling or active recovery helps stimulate blood flow after intense training days.'),
    9: ('Khoảng R–R nằm giữa hai đỉnh R liên tiếp trên sơ đồ ECG, cơ sở tính toán biến thiên nhịp tim (HRV).',
        'R-R interval between consecutive R-peaks on an ECG waveform, the basis for calculating HRV.'),
    10: ('Sơ đồ giải phẫu phế nang và mao mạch phổi, nơi diễn ra quá trình trao đổi khí trong từng nhịp thở.',
         'Anatomical diagram of pulmonary alveoli and capillaries where gas exchange occurs during breathing.'),
    11: ('Chuyển động của cơ hoành và khoang ngực giữa thì hít vào và thở ra khi đếm nhịp thở khi nghỉ.',
         'Movement of the diaphragm and thoracic cage between inhalation and exhalation when counting resting breaths.'),
    12: ('Ảnh minh họa buổi trao đổi và thăm khám với bác sĩ khi nhận thấy nhịp thở tăng hoặc có triệu chứng bất thường.',
         'Medical consultation illustrating when an elevated breathing rate or unusual symptoms warrant clinical evaluation.'),
    13: ('Một người tham gia ghi dữ liệu giấc ngủ với các điện cực.',
         'A person participating in sleep recording with electrodes.'),
    14: ('Mẫu nhật ký giấc ngủ theo dõi khung giờ đi ngủ và thức giấc để đánh giá tính nhất quán của lịch ngủ.',
         'Sleep diary template for tracking bedtime and wake time to evaluate sleep schedule consistency.'),
    15: ('Nằm nghỉ ngơi trên giường để cơ thể hồi phục sau những ngày tích lũy nợ ngủ.',
         'Resting in bed to allow the body to recover from accumulated sleep loss.'),
    16: ('Hypnogram minh họa các chu kỳ chuyển đổi giữa thức, giai đoạn REM và giấc ngủ sâu (NREM 3 / SWS).',
         'Hypnogram illustrating sleep stage cycles between wakefulness, REM and deep slow-wave sleep (NREM 3).'),
    17: ('Tập luyện kháng lực giúp bảo tồn khối nạc và sức mạnh cơ bắp bên cạnh việc theo dõi tỷ lệ mỡ cơ thể.',
         'Resistance training helps preserve lean mass and muscle strength alongside body fat monitoring.'),
    18: ('Các phần ăn được chuẩn bị sẵn: một ví dụ sắp xếp môi trường để bữa ăn thuận tiện hơn; không quy định khẩu phần cá nhân.',
         'Prepared meals illustrate making food easier to access; the photo does not prescribe individual portions.'),
    19: ('Một bữa ăn được chuẩn bị sẵn; ảnh không xác định đủ thành phần dinh dưỡng của khẩu phần.',
         'A prepared meal; the photo does not establish its nutritional composition.'),
    20: ('Cảm biến quang học ở mặt dưới một thiết bị đeo.',
         'An optical sensor on the underside of a wearable.'),
    21: ('Hai người nằm nghỉ trên giường.',
         'Two people resting in bed.'),
    22: ('Hai người trò chuyện trong một buổi tư vấn.',
         'Two people talking during a consultation.'),
    23: ('Một người ngồi yên trong tư thế thiền.',
         'A person sitting in a meditation posture.'),
    24: ('Một người tham gia ghi dữ liệu giấc ngủ với các điện cực.',
         'A person participating in sleep recording with electrodes.'),
    25: ('Cảm biến quang học phát sáng ở mặt dưới một đồng hồ.',
         'An illuminated optical sensor on a watch.'),
    26: ('Một người thực hiện bài tập vận động cánh tay.',
         'A person performing an arm exercise.'),
    27: ('Mặt nạ thu khí thở và hệ thống COSMED trong bố trí đo lường VO2 max và năng lực tim mạch.',
         'Breathing mask and COSMED metabolic cart measuring VO2 max and cardiorespiratory fitness.'),
    28: ('Thiết bị đo tín hiệu điện tim gắn đai ngực cung cấp bản ghi điện tim chính xác phục vụ theo dõi nhịp.',
         'Chest-worn cardiac sensor providing precise electrical recordings for heart rhythm monitoring.'),
    29: ('Đo huyết áp với vòng bít trong một buổi chăm sóc sức khỏe; ảnh minh họa phương pháp đo vật lý tiêu chuẩn.',
         'Blood pressure measurement with an upper-arm cuff during health care; illustrating the standard physical measurement.'),
}

TAKEAWAYS = [
    'Ghi thời lượng và mức gắng sức để phân bố tải tập phù hợp khả năng phục hồi.',
    'Xem nguồn dữ liệu và khoảng thiếu trước khi so số bước giữa các ngày.',
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
    'Xem thời gian ngủ cùng cảm giác tỉnh táo để chọn thay đổi phù hợp.',
    'Phân biệt lịch ngủ đều với thời gian trên giường và thời gian thực sự ngủ.',
    'Dành cơ hội ngủ phù hợp trong những ngày tiếp theo, không chỉ chờ nợ ngủ của ứng dụng về 0.',
    'Đọc số giờ và tỷ lệ REM/SWS cùng nhau; tỷ lệ cao hơn không tự bảo đảm ngủ tốt hơn.',
    'Kiểm tra nguồn, đơn vị và điều kiện đo khối nạc; khối nạc không đồng nghĩa khối cơ.',
    'Chọn một thói quen vừa sức và có thể lặp lại, thay vì tìm sáu mẹo bảo đảm giảm cân.',
    'Ưu tiên đủ năng lượng và chất dinh dưỡng trước khi tối ưu tỷ lệ macros từ một điểm Recovery.',
    'Đặt tín hiệu cơ thể cạnh cảm nhận và hoàn cảnh; không dùng chúng để chẩn đoán.',
    'Thử một thay đổi buổi tối có thể duy trì và theo dõi cả giấc ngủ lẫn cảm nhận ban ngày.',
    'Quan tâm cảm xúc, biểu hiện cơ thể và ảnh hưởng sinh hoạt cùng với dữ liệu thiết bị.',
    'Chọn một tình huống stress thường lặp lại và đánh giá việc nghỉ/thư giãn bằng trải nghiệm thực tế.',
    'Phân biệt nhu cầu ngủ, thời gian trên giường và thời gian thực sự ngủ.',
    'Phân biệt Live HR với dữ liệu qua đêm; khoảng tham chiếu không thay đánh giá triệu chứng.',
    'Ghi hiệp, lần lặp và mức tạ cùng cảm nhận để hiểu buổi tập.',
    'Tuổi sinh học là đầu ra của mô hình, không dự báo tuổi thọ cá nhân.',
    'Phân biệt ECG và sàng lọc bằng cảm biến quang học; kết quả bình thường không loại trừ mọi bệnh tim.',
    'Đo huyết áp bằng máy vòng bít phù hợp, ghi lại kết quả và không tự đổi thuốc.',
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
    source_labels.update({sid:s['display_label'] for sid,s in sources.items() if s.get('display_label')})
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
        body+=(f'\n> Bài biên soạn độc lập bởi Pulse & Vitality. Nội dung chỉnh ngày 29/10/2026; '
               f'nguồn đối chiếu {item["checked_on"]}. Liên kết được đặt tên theo chủ đề; tên tài liệu gốc và đơn vị phát hành có trên trang nguồn.\n')
        hero={}
        if n in HERO:
            source_art,role=HERO[n]
            hero=deepcopy(next(x for x in legacy[source_art]['image_attributions'] if x['role']==role))
            hero.update(article_id=aid,role='hero')
        # Captions are factual descriptions of the same, unmodified source asset.
        if hero and n in HERO_CAPTIONS:
            cap_vi, cap_en = HERO_CAPTIONS[n]
            hero.update(caption_vi=cap_vi, caption_en=cap_en)
        if hero:
            for lang in ['vi','en']:
                hero['alt_'+lang]=hero['caption_'+lang]
        category={'Recovery_Stress':'Recovery','Life_Heart_BP':'Health & Wellness',
                  'Healthspan_Body':'Health & Wellness'}.get(item['group'],item['group'])
        limitation='Điểm số và ước tính của thiết bị cần được đọc đúng bối cảnh; bài viết không xác nhận khả năng chẩn đoán hoặc điều trị.'
        if n in (28,29):
            limitation='Phân biệt phương pháp đo và nguồn dữ liệu; không dùng dữ liệu để tự chẩn đoán hoặc đổi thuốc.'
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
                            reader_revision=item.get('reader_revision',3),reader_revision_date=item.get('reader_revision_date','2026-10-27'),visual_policy='prose_first_no_text_card_diagram',
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
