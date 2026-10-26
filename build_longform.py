"""Develop the original topic outlines as full articles, with corrected evidence.

The baseline is retained for traceability; it is never blindly republished.
Editorial prose, examples, tables and source-specific research notes are editable
in data/longform_*. This module is called by rebuild_editorial.py.
"""
import csv
import json
from pathlib import Path
import re
import subprocess

BASE=Path(__file__).resolve().parent
ROOT=BASE.parent

def rows(name):
    with (BASE/'data'/name).open(encoding='utf-8',newline='') as f:
        return list(csv.DictReader(f,delimiter='\t'))

PRACTICE={
 'sleep': {
  'vi': '1. **Xác định vấn đề thật.** Phân biệt buồn ngủ ban ngày, khó ngủ, hay chỉ lo một chỉ số. Câu hỏi khác nhau cần cách theo dõi khác nhau.\n2. **Thử điều chỉnh có mục đích.** Chọn một thay đổi khả thi trong lịch hoặc môi trường, thay vì đổi nhiều yếu tố và mua nhiều sản phẩm cùng lúc.\n3. **Ghi cả trải nghiệm.** Thêm mức tỉnh táo và hoàn cảnh vào dữ liệu; đừng chỉ so hai điểm số hoặc hai hãng.\n4. **Đánh giá lại theo mục tiêu.** Một biểu đồ đẹp hơn nhưng vẫn buồn ngủ nhiều chưa phải kết quả đủ. Không trì hoãn tư vấn khi có triệu chứng đáng lo.',
  'en': '1. **Define the real problem.** Daytime sleepiness, difficulty sleeping and worry about a metric need different questions.\n2. **Make a purposeful adjustment.** Choose one feasible routine or environment change rather than changing everything or buying several products.\n3. **Record experience too.** Note alertness and context, not just scores from different brands.\n4. **Review against the goal.** A better graph with persistent sleepiness is not enough. Do not delay advice for concerning symptoms.'},
 'data': {
  'vi': '1. **Kiểm tra bạn đang xem gì.** Xác định tên chỉ số, cách thiết bị lấy mẫu và điều kiện đo trước khi so sánh.\n2. **Đặt cạnh bối cảnh.** Ghi giấc ngủ, vận động, bệnh gần đây, thuốc và cảm giác; nhiều yếu tố có thể thay đổi cùng lúc.\n3. **Chọn phản ứng phù hợp.** Điều chỉnh để hỗ trợ sức khỏe hoặc sự dễ chịu, không để ép một đường cong đạt mục tiêu.\n4. **Xem diễn biến.** Mẫu nhiều lần đo hữu ích hơn một điểm đơn lẻ, nhưng triệu chứng mới hoặc nặng không cần chờ đủ số ngày mới được đánh giá.',
  'en': '1. **Identify the measurement.** Check the metric, sampling and conditions before comparing.\n2. **Add context.** Sleep, activity, illness, medicines and feelings can change together.\n3. **Choose an appropriate response.** Support health or comfort rather than forcing a graph toward a target.\n4. **Review the course.** Repeated observations are useful, but new or substantial symptoms need not wait for enough tracking days.'},
 'activity': {
  'vi': '1. **Nêu mục đích buổi tập.** Phát triển sức bền, sức mạnh hoặc phục hồi không cần cùng một mức gắng sức.\n2. **Giữ dữ liệu công việc thực tế.** Ghi loại bài, thời lượng hoặc số hiệp cùng cảm giác, để điểm tải không tách khỏi điều đã làm.\n3. **Điều chỉnh theo phản ứng.** Nóng, ngủ kém, đau hoặc bệnh có thể khiến mức phù hợp hôm nay khác hôm trước.\n4. **Xem khả năng duy trì.** Tiến triển có ý nghĩa gồm hoạt động dễ hơn và hồi phục phù hợp; tăng điểm không phải mục tiêu sức khỏe độc lập.',
  'en': '1. **State the session purpose.** Endurance, strength and recovery do not require identical effort.\n2. **Keep the actual work record.** Add activity, time or sets and effort alongside load scores.\n3. **Respond to conditions.** Heat, poor sleep, pain or illness can change a suitable workload.\n4. **Consider sustainability.** Easier function and appropriate recovery matter; more points are not an independent health goal.'},
 'women': {
  'vi': '1. **Ghi điều ảnh hưởng cuộc sống.** Thời điểm, đau, chảy máu, giấc ngủ hoặc mức khó chịu cụ thể giúp làm rõ câu hỏi.\n2. **Ghi những thay đổi liên quan.** Thuốc, tránh thai, lịch sống, khả năng mang thai và giai đoạn sau sinh có thể đổi cách diễn giải.\n3. **Chọn hỗ trợ theo mục tiêu.** Có thai, tránh thai, giảm đau và điều chỉnh tập là những mục tiêu khác nhau; không dùng một biểu đồ thay cho mọi quyết định.\n4. **Chuẩn bị trao đổi khi cần.** Mang diễn biến và điều đã thử, hỏi rõ lựa chọn cùng kế hoạch theo dõi thay vì tự mua một bộ xét nghiệm hoặc phác đồ bổ sung.',
  'en': '1. **Record the impact.** Timing, pain, bleeding, sleep and specific difficulties help clarify the question.\n2. **Note relevant changes.** Medicines, contraception, pregnancy possibility, routine and postpartum status affect interpretation.\n3. **Match support to the goal.** Conception, contraception, pain relief and training adjustment require different decisions.\n4. **Prepare for advice.** Bring the course and measures tried, and discuss options and follow-up rather than ordering a broad panel or supplement protocol.'},
 'nutrition': {
  'vi': '1. **Nhìn toàn bộ khẩu phần.** Tính cả thực phẩm, đồ uống và viên bổ sung, thay vì chỉ một chất nổi bật trong quảng cáo.\n2. **Gắn với hoàn cảnh thật.** Khối lượng tập, khả năng nấu ăn, điều kiện kinh tế và bệnh nền quyết định tính khả thi.\n3. **Đổi một việc có thể duy trì.** Ví dụ, chuẩn bị bữa phù hợp hơn hoặc xem lại thành phần chồng lặp; không coi mức hạn chế nghiêm ngặt là thành tích sức khỏe.\n4. **Đánh giá đúng kết quả.** Cảm giác và khả năng sinh hoạt khác với kết quả xét nghiệm hay sinh sản; khi cần hãy trao đổi mục tiêu theo dõi phù hợp.',
  'en': '1. **Review the whole intake.** Include food, drinks and overlapping supplements rather than one promoted nutrient.\n2. **Account for real circumstances.** Training, cooking, affordability and health shape feasibility.\n3. **Change something sustainable.** Improve meal preparation or remove ingredient overlap rather than treating strict restriction as a health achievement.\n4. **Use the right outcome.** Daily function differs from laboratory or fertility outcomes; discuss suitable monitoring when needed.'},
 'relationship': {
  'vi': '1. **Chọn một tình huống cụ thể.** Mô tả điều xảy ra và nhu cầu thay vì gán tính cách hoặc chẩn đoán trạng thái thần kinh của đối phương.\n2. **Kiểm tra mình đã hiểu đúng.** Hỏi lại hoặc tóm tắt trước khi phản hồi; việc lắng nghe không đồng nghĩa buộc phải đồng ý mọi yêu cầu.\n3. **Thống nhất một việc nhỏ, tự nguyện.** Có thể là cách báo cần nghỉ hoặc thời điểm trao đổi, với quyền thay đổi và đặt ranh giới.\n4. **Xem tác động thực tế.** Tôn trọng và an toàn quan trọng hơn hoàn thành bài tập hay đạt tỷ lệ tương tác. Khi có ép buộc, ưu tiên hỗ trợ riêng.',
  'en': '1. **Choose one situation.** Describe events and needs rather than diagnosing a partner\'s character or nervous system.\n2. **Check understanding.** Ask or paraphrase before replying; listening does not require accepting every request.\n3. **Agree one voluntary action.** Discuss a pause or conversation time with boundaries and room to change.\n4. **Assess actual impact.** Respect and safety matter more than completing an exercise or meeting a ratio. Coercion calls for individual support.'},
 'sexual': {
  'vi': '1. **Mô tả thay đổi và mức khó chịu.** Ghi thời điểm bắt đầu, hoàn cảnh và triệu chứng, không chỉ một con số hiệu suất.\n2. **Xem cả sức khỏe và bối cảnh.** Thuốc, đau, mệt, lo lắng và quan hệ có thể cùng góp phần; không cần chọn duy nhất tâm lý hay cơ thể.\n3. **Trao đổi cách gần gũi thoải mái.** Không biến cương, cực khoái hoặc thời gian thành nghĩa vụ; quyền dừng và lời từ chối luôn có giá trị.\n4. **Tìm hỗ trợ đúng vấn đề.** Khi kéo dài hoặc gây khổ sở, có thể cần đánh giá y khoa, tư vấn hoặc phục hồi phù hợp; tránh tự dùng hormone hoặc sản phẩm không rõ thành phần.',
  'en': '1. **Describe change and distress.** Note onset, context and symptoms rather than one performance number.\n2. **Consider health and circumstances.** Medication, pain, fatigue, anxiety and relationships can coexist.\n3. **Discuss comfortable intimacy.** Erections, orgasm and duration are not obligations; consent and the option to stop remain essential.\n4. **Seek appropriate support.** Persistent distress may need medical care, counselling or rehabilitation rather than self-prescribed hormones or unclear products.'}
}

def first_paragraph(body):
    body=re.sub(r'<figure\b[\s\S]*?</figure>','',body)
    return next(p.strip() for p in re.split(r'\n\s*\n',body) if p.strip() and not p.startswith('#'))

def baseline():
    local=ROOT/'audit/health-2026-10-26/before/articles.json'
    if local.exists():return json.loads(local.read_text())
    result=subprocess.run(['git','show','f68c786:articles.json'],cwd=BASE,check=True,capture_output=True,text=True)
    return json.loads(result.stdout)

def build(sources,catalog):
    old={a['id']:a for a in baseline()}
    cases={r['id']:r for name in ['longform_cases.tsv','longform_extra_cases.tsv'] for r in rows(name)}
    modules={r['id']:r for name in ['longform_modules.tsv','longform_women_modules.tsv','longform_men_modules.tsv'] for r in rows(name)}
    for extension in rows('longform_extensions.tsv'):
        module=modules[extension['module']]
        for lang in ['vi','en']:
            module['body_'+lang]+='\\n\\n'+extension['body_'+lang]
        module['sources']=','.join(dict.fromkeys((module['sources']+','+extension['sources']).split(',')))
    tables=json.loads((BASE/'data/longform_tables.json').read_text())
    research=json.loads((BASE/'data/longform_research.json').read_text())
    assert set(cases)==set(old)==set(catalog)
    records={}
    # Restore actual introductory passages where they are descriptive rather
    # than the unverified numerical/treatment claims corrected in this edition.
    original_hooks={'LM_SL_02','LM_RC_01','LM_RC_02','DM_HW_01','WH_13','WH_15','WH_18','WH_23'}
    restored_figures={
        'LM_SL_01':('Thiết lập ghi đa ký giấc ngủ; khác với cảm biến đồng hồ phổ thông.','A polysomnography recording setup; different from ordinary watch sensors.'),
        'LM_SL_02':('Ví dụ hypnogram minh họa các giai đoạn; không phải dữ liệu của người đọc.','An example hypnogram illustrating stages, not the reader\'s measurements.'),
        'DM_SL_01':('Minh họa tín hiệu điện não giấc ngủ sóng chậm; tên giai đoạn trong hình có thể theo phân loại cũ.','Illustrative slow-wave sleep EEG; stage labels may reflect an older classification.'),
        'LM_RC_01':('Khoảng R–R trên điện tim, minh họa khái niệm khoảng nhịp.','An ECG R–R interval illustrating beat timing.'),
        'LM_RC_02':('Các yếu tố của cung lượng tim; không suy trực tiếp từng yếu tố từ mạch cổ tay.','Cardiac-output factors, not separately measured from wrist pulse.'),
        'LM_HW_02':('Đo trao đổi khí khi vận động; phân biệt với VO2 max ước tính trên thiết bị đeo.','Exercise gas-exchange assessment, distinct from wearable VO2 max estimates.'),
        'LM_WH_01':('Mô hình chu kỳ minh họa; ngày và đường cong không phải dự báo cá nhân.','An illustrative cycle model; timing and curves are not personal predictions.'),
        'LM_WH_02':('Giải phẫu cơ quan sinh sản nữ và vị trí cổ tử cung.','Female reproductive anatomy and the position of the cervix.'),
        'LM_WH_03':('Minh họa các quá trình trong chu kỳ; không dùng hình để xác nhận rụng trứng cá nhân.','Cycle processes illustrated, not an individual ovulation test.'),
        'WH_12':('Minh họa giải phẫu vùng đáy chậu nữ; không tự chẩn đoán nguồn đau từ hình.','Female perineal anatomy; an image cannot diagnose a pain source.'),
        'WH_13':('Minh họa nhóm cơ sàn chậu và vị trí nâng đỡ.','Pelvic-floor muscles and their supporting position.'),
        'WH_22':('Sơ đồ chuyển hóa sắt; không phải bảng mục tiêu xét nghiệm cá nhân.','Iron handling illustrated, not personal laboratory targets.'),
        'WH_24':('Minh họa phôi nang; không phải hình xác nhận làm tổ của người đọc.','A blastocyst illustration, not confirmation of implantation.'),
        'WH_25':('Giải phẫu nhau thai minh họa trao đổi mẹ–thai.','Placental anatomy illustrating maternal–fetal exchange.'),
        'WH_27':('Ví dụ siêu âm thành bụng; không thay đánh giá triệu chứng và chức năng.','An abdominal-wall ultrasound example, not a substitute for functional assessment.'),
        'WH_29':('Minh họa vị trí tổn thương lạc nội mạc tử cung; không chẩn đoán bằng hình minh họa.','Illustrative endometriosis locations, not a diagnostic image.'),
        'MW_NUT_01':('Sơ đồ tạo hormone steroid; không hàm ý ăn nhiều cholesterol sẽ tăng testosterone.','Steroid synthesis illustrated; more dietary cholesterol does not guarantee more testosterone.'),
        'MW_NUT_04':('Minh họa chuyển hóa ethanol; không định lượng tổn hại cá nhân từ số ly.','Ethanol metabolism illustrated, not individual harm quantified by drinks.'),
        'MW_NUT_06':('Cấu trúc tinh trùng minh họa; không dự đoán khả năng có con.','Sperm anatomy illustrated, not a fertility prediction.'),
        'MW_SXH_08':('Trục điều hòa sinh sản minh họa; xét nghiệm cần diễn giải theo bối cảnh.','Reproductive regulation illustrated; laboratory interpretation requires context.'),
        'MW_SXO_02':('Đường truyền tín hiệu giãn cơ trơn minh họa; không phải kết quả xét nghiệm.','An illustrative smooth-muscle relaxation pathway, not a test result.'),
        'MW_SXO_05':('Giải phẫu cơ vùng đáy chậu nam; không chứng minh có kỹ thuật khóa phản xạ.','Male perineal anatomy, not proof of a reflex-lock technique.')
    }
    for aid,case in cases.items():
        row=catalog[aid];original=old[aid]
        mids=case['modules'].split(',')
        # Longer original metric explainers retain the broader explanatory arc.
        if aid.startswith(('LM_SL','DM_SL')):
            for m in ['sleep_sensors','sleep_architecture','sleep_pressure','sleep_debt']:
                if m not in mids:mids.append(m)
        if aid=='LM_RC_01':mids.append('breathing_physiology')
        if aid=='LM_RC_02':mids.append('vo2_physiology')
        if aid=='LM_AC_02':mids.append('recovery_mechanism')
        if aid=='LM_HW_02':mids.append('intensity_methods')
        mids=list(dict.fromkeys(mids))
        refids=list(dict.fromkeys(row['sources'].split(',')+[s for m in mids for s in modules[m]['sources'].split(',')]+research.get(aid,{}).get('sources',[])))
        if aid=='LM_MH_03':
            refids=['dorey_trial','pastore_study']+[r for r in refids if r not in ['dorey_trial','pastore_study']]
        refs=[dict(sources[k],checked_date='2026-10-26') for k in refids]
        number={r['id']:n for n,r in enumerate(refs,1)}
        def cites(ids):return ' '.join(f'[{number[k]}]({sources[k]["url"]})' for k in dict.fromkeys(ids))
        content={}
        for lang in ['vi','en']:
            parts=[]
            if aid in original_hooks:
                parts.append(first_paragraph(original['content_vi' if lang=='vi' else 'content']))
            parts.append(row['facts_'+lang])
            parts.append(('**Tình huống minh họa:** ' if lang=='vi' else '**Illustrative situation:** ')+case['case_'+lang])
            for mid in mids:
                module=modules[mid]
                parts += ['## '+module['title_'+lang],module['body_'+lang].replace('\\n','\n')+' '+cites(module['sources'].split(','))]
            table_key=next((mid for mid in mids if mid in tables),None)
            if table_key:
                parts += ['## '+('Bảng đối chiếu để đọc đúng thông tin' if lang=='vi' else 'A comparison for practical interpretation'),tables[table_key][lang]]
            if aid in research:
                parts += ['## '+('Đối chiếu tài liệu gốc: kết quả và giới hạn' if lang=='vi' else 'Checking the original sources: findings and limits'),research[aid][lang],cites(research[aid]['sources'])]
            elif any(r['kind'] in ['Systematic review and meta-analysis','Systematic review','Randomized remote trial','Small experimental study','Observational cohort'] for r in refs):
                # Article-specific limitations remain adjacent to the evidence.
                parts += ['## '+('Điểm cần giữ khi đọc kết quả nghiên cứu' if lang=='vi' else 'Keeping research findings in context'),row['limits_'+lang]+' '+cites(refids[:min(3,len(refids))])]
            category=original['category']
            kind='sleep' if category=='Sleep' else 'activity' if category=='Activity' else 'women' if category=="Women's Health" else 'data'
            if aid.startswith('MW_NUT'):kind='nutrition'
            elif aid.startswith('MW_REL'):kind='relationship'
            elif category=="Men's Health":kind='sexual'
            parts += ['## '+('Ứng dụng thực tế: làm gì và đánh giá bằng cách nào?' if lang=='vi' else 'Putting this into practice and evaluating the response'),row['action_'+lang],PRACTICE[kind][lang]]
            parts += ['## '+('Khi nào nên tìm hỗ trợ?' if lang=='vi' else 'When to seek support'),row['limits_'+lang],row['care_'+lang]]
            parts += ['## '+('Nguồn tham khảo và phạm vi hỗ trợ' if lang=='vi' else 'References and what they support')]
            for n,ref in enumerate(refs,1):
                parts.append(f'{n}. [{ref["title"]}]({ref["url"]}) — {ref["kind"]}. '+('Hỗ trợ: ' if lang=='vi' else 'Supports: ')+ref['support_'+lang]+'.')
            parts.append('> Cập nhật nội dung và nguồn: 26/10/2026. Nội dung giáo dục; chưa có xác nhận duyệt bởi bác sĩ.' if lang=='vi' else '> Content and sources updated: 26 October 2026. Educational content; clinical sign-off has not been recorded.')
            content[lang]='\n\n'.join(parts)+'\n'
        record={
            'content':content['en'],'content_vi':content['vi'],'references':refs,
            'hero_image':original['hero_image'],'thumbnail':original['hero_image'],
            'hero_image_source_url':'https://test-repo-y1wb.onrender.com/'+original['hero_image'],
            'image_provenance':'Hero restored from the original project library. Retained diagrams are illustrations, not study outcome data. Summary guidance is article text, not an image.',
            'inline_image':'','inline_image_source_url':'','inline_caption_vi':'','inline_caption':'',
            'baseline_revision':'f68c786','content_edition':'Long-form development of the original topic outline',
            'baseline_headings_vi':re.findall(r'^## (.+)',original['content_vi'],re.M),
            'longform_modules':mids,
        }
        if aid in restored_figures:
            record.update(inline_image=original['inline_image'],inline_image_source_url='https://test-repo-y1wb.onrender.com/'+original['inline_image'],
                          inline_caption_vi=restored_figures[aid][0],inline_caption=restored_figures[aid][1])
        records[aid]=record
    from image_curation import apply_image_selections
    apply_image_selections(records)
    (BASE/'data/longform_articles.json').write_text(json.dumps(records,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    return records
