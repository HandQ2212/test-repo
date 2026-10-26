# Kết quả rà soát nội dung sức khỏe — 26/10/2026

Bản cũ **chưa đáp ứng yêu cầu chính xác và hữu ích để xuất bản như nội dung đã được xác thực y khoa**. Có link dẫn sai nghiên cứu, suy diễn sinh học quá mức, chú thích ảnh không khớp và tuyên bố về người duyệt chưa có căn cứ. Bản sửa chuyển sang hướng dẫn giáo dục ngắn gọn, có hành động thực tế, giới hạn và dấu hiệu cần khám.

## Phạm vi và kết quả

- 83 bài, đầy đủ bản Việt và Anh, giữ nguyên Content_ID để không đổi đường dẫn.
- Đối chiếu 480 URL cũ, gồm tài liệu và nguồn ảnh. HTTP: 211 trả 200, 187 trả 203/challenge, 70 trả 403, 10 trả 404, 2 trả 202. Đây là kết quả truy cập, không phải phép chấm chất lượng y khoa.
- Tra metadata của 187 PMID cũ qua Europe PMC; nhận 185 bản ghi. Hai bản ghi chưa trả về không được tự coi là hợp lệ.
- Xác nhận ít nhất 29 **bài có PMID nguồn chính không liên quan** bằng tên nghiên cứu thực tế; bảng chi tiết ở cuối báo cáo.
- Thay danh mục hoạt động bằng 70 nguồn: hướng dẫn cơ quan y tế, hội chuyên môn, tổng quan, nghiên cứu gốc và tài liệu hãng. Ghi rõ loại và phạm vi hỗ trợ. Không gọi mọi tài liệu hãng là nghiên cứu lâm sàng.
- Kiểm tra 70 URL nguồn hiện tại: 42 trả HTTP 200, 20 PubMed trả HTTP 203/challenge, 8 trả 403 từ bộ kiểm tra tự động; không có 404 trong danh mục mới. PMID được đối chiếu riêng với metadata, không dựa vào HTTP 203. Các nguồn bị chặn tự động được kiểm tra bằng trang chính thức hoặc nội dung chỉ mục tương ứng; không tuyên bố đã đọc toàn bộ full text của mọi nghiên cứu.
- Thay 166 hình đang hiển thị bằng SVG do dự án tạo, ghi rõ minh họa biên tập. Không còn gắn nhãn Unsplash/Wikimedia cho hình không xác minh được nguồn, nội dung và quyền sử dụng.
- Cập nhật master Excel, hai roadmap và ba bản tải xuống trong website. Các sheet cũ được giữ, trường nội dung/nguồn được sửa; thêm bảng audit và nguồn.

## Nội dung đã sửa

1. Bỏ bảng trọng số điểm ngủ dùng chung cho nhiều hãng; phân biệt ước tính thiết bị với đa ký giấc ngủ. Không dùng một điểm để cấp phép tập nặng.
2. Bỏ suy diễn HRV/nhịp tim thành cortisol, testosterone, estrogen, serotonin, làm tổ hoặc xác nhận thai. Sửa cả metadata mapping vốn làm các cơ chế này trông như chỉ số đo được.
3. Bỏ lịch tập, chế độ ăn theo pha và các tỷ lệ hormone bắt buộc cho mọi người. Nêu rõ biến thiên cá nhân và giới hạn nghiên cứu.
4. Bỏ hướng dẫn tự dùng vi chất liều cao, mẹo khóa xuất tinh bảo đảm hiệu quả và lời hứa tăng testosterone. Nêu rõ vai trò thả lỏng sàn chậu, đánh giá nguyên nhân và kế hoạch có con khi bàn hormone.
5. Phân biệt tương quan với nhân quả trong nội dung sauna, quan hệ, giấc ngủ và dinh dưỡng sinh sản. Thử nghiệm nhỏ không được quy đổi thành tuổi sinh học hoặc tỷ lệ cải thiện chắc chắn.
6. Thay tiêu đề giật mức, mô tả, takeaway và nội dung ở cả hai ngôn ngữ. Mỗi bài có phần hiểu đúng, thực hành, giới hạn, lúc cần tư vấn và tài liệu kèm phạm vi hỗ trợ.
7. Bỏ nhãn “Clinical Editorial Board”, “hội đồng biên tập y khoa” và “hình xác thực 100%” chưa có thông tin chứng minh. Trạng thái duyệt bởi bác sĩ được ghi đúng là **chưa có xác nhận**.

## Hình ảnh

Ảnh và sơ đồ được xem bằng contact sheet cho toàn bộ thư viện cũ. Ví dụ không phù hợp:

- `LM_AC_02`: hình CO2/đáp ứng dịch trong hồi sức không giải thích WHOOP Day Strain.
- `WH_26`: hình thủ thuật sản khoa không hướng dẫn tập luyện thai kỳ.
- `MW_REL_01`: sơ đồ giải phẫu thần kinh không chứng minh tỷ lệ giao tiếp 5:1.
- `DM_SL_02`: công thức phân tử melatonin không giải thích nợ ngủ.

Hình mới tóm tắt nội dung đúng chủ đề và không chứa số liệu bệnh nhân, kết quả thí nghiệm hoặc giải phẫu tự suy diễn. Đây là lựa chọn minh họa biên tập cho bản giáo dục cơ bản. Nếu bổ sung hình giải phẫu hay biểu đồ định lượng trong tương lai, cần đối chiếu nội dung, chú thích, tác giả và giấy phép cụ thể.

## File và khả năng kiểm tra lại

- `Master_Content_MVP`: 83 hàng nội dung đã sửa, danh mục nguồn JSON, giới hạn bằng chứng, ngày rà soát, trạng thái duyệt và URL bài.
- `Mapping_Matrix`: tiêu đề, chủ đề và nguồn chính khớp dữ liệu website.
- `HDSD_Data_Schema`: bỏ link mẫu và ví dụ PMID sai; phân biệt nguồn minh họa với nguồn nghiên cứu.
- `Editorial_Audit`: 83 hàng, lưu phát hiện và cách sửa, nguồn cũ/mới, tiêu đề thực của PMID cũ, giới hạn và đường dẫn bài.
- `Source_Register`: 70 nguồn, URL bấm được, loại nguồn và phạm vi hỗ trợ.
- `Link_Audit`: kết quả truy cập 480 URL cũ; các nguồn cũ trong sheet này được giữ làm bằng chứng audit, không phải nguồn đang dùng.
- Hai roadmap: sửa cả trường đang có và thêm `Reviewed_Content`, `Source_Register`. Women's roadmap có 30 hàng ánh xạ tới 28 ID khác nhau; hai cặp dùng chung bài là `LM_WH_01` và `DM_WH_03`, không phải 30 bài độc lập trong roadmap này.
- Bản cũ được giữ trong lịch sử Git và thư mục `audit/health-2026-10-26/before` ở workspace. Không có thay đổi xóa lịch sử.

## Kiểm tra kỹ thuật

- Kiểm tra 83 ID duy nhất, đủ nội dung Việt/Anh, nguồn chính thuộc danh mục đầy đủ, URL nghiên cứu khớp tên metadata, và các PMID sai xác nhận không quay lại bài tương ứng.
- Kiểm tra JSON/JS/Markdown/Excel/HTML khớp nhau, ba workbook local và bản tải xuống có nội dung byte giống nhau, toàn bộ ảnh tồn tại, SVG hợp lệ, ảnh có alt và đường dẫn HTML tương đối đúng.
- Chrome: mở toàn bộ 83 bài trong SPA ở cả hai ngôn ngữ; kiểm tra 166 ảnh, 83 trang HTML, tìm kiếm, popup và chuyển ngôn ngữ. Kiểm tra mobile 390 px, không tràn ngang trang và không có lỗi JavaScript.
- Sửa lỗi CSS cũ thiếu quy tắc `.hidden`, khiến trang HTML hiện cả Việt lẫn Anh và phần bài mẫu trên trang chủ.
- Kiểm tra cú pháp JavaScript và Git diff whitespace. Kiểm tra lại bản live sau khi đẩy lên Render được ghi riêng trong workspace.

## Giới hạn còn lại

Đây là rà soát biên tập dựa trên nguồn, không phải nghiên cứu hệ thống mới hoặc xác nhận của bác sĩ. Bản sửa phù hợp làm kiến thức giáo dục cơ bản, không chẩn đoán người dùng hoặc kê điều trị cá nhân. Chưa có người duyệt lâm sàng được xác nhận; không thể gọi dữ liệu “chính xác 100%”. Nguồn có thể đổi sau ngày kiểm tra. Các bài được rút gọn để bỏ nội dung suy diễn; nếu mở rộng lại cần kiểm tra từng luận điểm mới thay vì tái chạy các script tạo bản nháp cũ.

## Những PMID nguồn chính đã xác nhận sai chủ đề

| Content ID | Nghiên cứu thực tế của link cũ | Nguồn chính đã thay |
|---|---|---|
| LM_SL_01 | [Multiple sclerosis: A possible link between multiple sclerosis and gut microbiota.](https://pubmed.ncbi.nlm.nih.gov/28960186/) | [Nguồn thay thế](https://pubmed.ncbi.nlm.nih.gov/34314344/) |
| LM_RC_02 | [Acute effects of posture on intraocular pressure.](https://pubmed.ncbi.nlm.nih.gov/32027692/) | [Nguồn thay thế](https://www.heart.org/en/health-topics/high-blood-pressure/the-facts-about-high-blood-pressure/all-about-heart-rate-pulse) |
| LM_HW_01 | [What does fMRI tell us about neuronal activity?](https://pubmed.ncbi.nlm.nih.gov/11836522/) | [Nguồn thay thế](https://pubmed.ncbi.nlm.nih.gov/27680542/) |
| LM_HW_02 | [Estimated Change in Prevalence of Hypertension in Nepal Following Application of the 2017 ACC/AHA Guideline.](https://pubmed.ncbi.nlm.nih.gov/30646022/) | [Nguồn thay thế](https://pubmed.ncbi.nlm.nih.gov/27881567/) |
| LM_WH_01 | [Individual Variation in Functional Topography of Association Networks in Youth.](https://pubmed.ncbi.nlm.nih.gov/32078800/) | [Nguồn thay thế](https://www.nhs.uk/conditions/periods/) |
| LM_WH_02 | [Fluorescence in situ hybridization analysis of two blastomeres from day 3 frozen-thawed embryos followed by analysis of the remaining embryo on day 5.](https://pubmed.ncbi.nlm.nih.gov/14998971/) | [Nguồn thay thế](https://www.acog.org/womens-health/faqs/fertility-awareness-based-methods-of-family-planning) |
| LM_WH_03 | [Description of Residual Stress and Strain Fields in FGM Hollow Disc Subject to External Pressure.](https://pubmed.ncbi.nlm.nih.gov/30709005/) | [Nguồn thay thế](https://www.acog.org/womens-health/faqs/fertility-awareness-based-methods-of-family-planning) |
| DM_WH_01 | [Acceptability and willingness among men who have sex with men (MSM) to use a tablet-based HIV risk assessment in a clinical setting.](https://pubmed.ncbi.nlm.nih.gov/25525569/) | [Nguồn thay thế](https://pubmed.ncbi.nlm.nih.gov/32661839/) |
| LM_MH_01 | [A varying-coefficient Cox model for the effect of age at a marker event on age at menopause.](https://pubmed.ncbi.nlm.nih.gov/16011707/) | [Nguồn thay thế](https://www.nth.nhs.uk/resources/pelvic-floor-exercises-for-men/) |
| LM_MH_03 | [Influence of ionizing radiation on ovarian carcinoma SKOV- 3 xenografts in nude mice under hypoxic conditions.](https://pubmed.ncbi.nlm.nih.gov/24716983/) | [Nguồn thay thế](https://www.royalberkshire.nhs.uk/media/avwg3hls/pelvic-floor-strengthening-and-relaxation-exercises-for-men_jun24.pdf) |
| DM_MH_01 | [Influence of ionizing radiation on ovarian carcinoma SKOV- 3 xenografts in nude mice under hypoxic conditions.](https://pubmed.ncbi.nlm.nih.gov/24716983/) | [Nguồn thay thế](https://www.nhs.uk/conditions/ejaculation-problems/) |
| DM_MH_03 | [Determinants of cancer disparities: barriers to cancer screening, diagnosis, and treatment.](https://pubmed.ncbi.nlm.nih.gov/16226685/) | [Nguồn thay thế](https://www.niddk.nih.gov/health-information/urologic-diseases/erectile-dysfunction/symptoms-causes) |
| WH_06 | [Visualizing induced silent steam pop with intracardiac echocardiography.](https://pubmed.ncbi.nlm.nih.gov/28430939/) | [Nguồn thay thế](https://www.endocrine.org/patient-engagement/endocrine-library/hormones-and-endocrine-function/reproductive-hormones) |
| WH_07 | [Diagnostic accuracy of anaesthesiologists' prediction of difficult airway management in daily clinical practice: a cohort study of 188 064 patients registered in the Danish Anaesthesia Database.](https://pubmed.ncbi.nlm.nih.gov/25511370/) | [Nguồn thay thế](https://www.nhs.uk/conditions/pre-menstrual-syndrome/) |
| WH_09 | [Folate levels and N(5),N(10)-methylenetetrahydrofolate reductase genotype (MTHFR) in mothers of offspring with neural tube defects: a case-control study.](https://pubmed.ncbi.nlm.nih.gov/11440783/) | [Nguồn thay thế](https://www.nhs.uk/symptoms/loss-of-libido/) |
| WH_10 | [CFD modelling of the aerodynamic effect of trees on urban air pollution dispersion.](https://pubmed.ncbi.nlm.nih.gov/23751336/) | [Nguồn thay thế](https://www.nhs.uk/conditions/pre-menstrual-syndrome/) |
| MW_NUT_02 | [Conjugated equine estrogens and global cognitive function in postmenopausal women: Women's Health Initiative Memory Study.](https://pubmed.ncbi.nlm.nih.gov/15213207/) | [Nguồn thay thế](https://www.who.int/news-room/fact-sheets/detail/healthy-diet) |
| MW_NUT_04 | [Characteristics of an 'effective' tackle outcome in Six Nations rugby.](https://pubmed.ncbi.nlm.nih.gov/24533518/) | [Nguồn thay thế](https://www.who.int/news-room/fact-sheets/detail/alcohol) |
| MW_SXH_04 | [Synthesis of beta-SiC/SiO2 core-sheath nanowires by CVD technique using Ni as catalyst.](https://pubmed.ncbi.nlm.nih.gov/20358897/) | [Nguồn thay thế](https://www.niddk.nih.gov/health-information/urologic-diseases/erectile-dysfunction/symptoms-causes) |
| MW_REL_03 | [Common coding of auditory and visual spatial information in working memory.](https://pubmed.ncbi.nlm.nih.gov/18652807/) | [Nguồn thay thế](https://www.nhs.uk/every-mind-matters/lifes-challenges/maintaining-healthy-relationships-and-mental-wellbeing/) |
| MW_REL_04 | [A randomised controlled trial of intervention site radiotherapy in malignant pleural mesothelioma.](https://pubmed.ncbi.nlm.nih.gov/17588698/) | [Nguồn thay thế](https://www.nhs.uk/every-mind-matters/lifes-challenges/maintaining-healthy-relationships-and-mental-wellbeing/) |
| MW_SXO_01 | [Acute myocardial infarction in developing countries: the importance of large national registries.](https://pubmed.ncbi.nlm.nih.gov/17397950/) | [Nguồn thay thế](https://www.nhs.uk/symptoms/loss-of-libido/) |
| MW_SXO_04 | [Late onset of CAD gene amplification in unamplified PALA resistant Chinese hamster mutants.](https://pubmed.ncbi.nlm.nih.gov/10704733/) | [Nguồn thay thế](https://www.nhs.uk/symptoms/loss-of-libido/) |
| MW_SXH_05 | [Achieving "proper" satiety in different social contexts--qualitative interpretations from a cross-disciplinary project, sociomaet.](https://pubmed.ncbi.nlm.nih.gov/12495694/) | [Nguồn thay thế](https://www.niddk.nih.gov/health-information/urologic-diseases/erectile-dysfunction/symptoms-causes) |
| MW_SXH_06 | [Synthesis and comparison of antioxidant properties of indole-based melatonin analogue indole amino Acid derivatives.](https://pubmed.ncbi.nlm.nih.gov/21883955/) | [Nguồn thay thế](https://www.niddk.nih.gov/health-information/urologic-diseases/erectile-dysfunction/treatment) |
| MW_SXH_07 | [Familial and sporadic breast cancers: differences in clinical, histopathological, and immunohistochemical features.](https://pubmed.ncbi.nlm.nih.gov/20308044/) | [Nguồn thay thế](https://integration.asrm.org/practice-guidance/practice-committee-documents/diagnosis-and-treatment-of-infertility-in-men-aua-asrm-guideline-part2/) |
| MW_REL_07 | [Common coding of auditory and visual spatial information in working memory.](https://pubmed.ncbi.nlm.nih.gov/18652807/) | [Nguồn thay thế](https://www.nhs.uk/every-mind-matters/lifes-challenges/maintaining-healthy-relationships-and-mental-wellbeing/) |
| MW_REL_08 | [A modified operational sequence methodology for zoo exhibit design and renovation: conceptualizing animals, staff, and visitors as interdependent coworkers.](https://pubmed.ncbi.nlm.nih.gov/24838689/) | [Nguồn thay thế](https://pubmed.ncbi.nlm.nih.gov/39514915/) |
| MW_SXO_05 | [Age-related changes in primary somatosensory cortex of rats: evidence for parallel degenerative and plastic-adaptive processes.](https://pubmed.ncbi.nlm.nih.gov/12470685/) | [Nguồn thay thế](https://www.nhs.uk/conditions/ejaculation-problems/) |
