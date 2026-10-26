# Kết quả rà soát nội dung sức khỏe — 26/10/2026

Bản cũ **chưa đáp ứng yêu cầu chính xác và hữu ích để xuất bản như nội dung đã được xác thực y khoa**. Có link dẫn sai nghiên cứu, suy diễn sinh học quá mức, chú thích ảnh không khớp và tuyên bố về người duyệt chưa có căn cứ. Sau phản hồi về việc rút gọn quá mức, bản hiện tại phát triển lại bài chuyên sâu theo mạch chủ đề gốc ở commit `f68c786`: giải thích cơ chế, ví dụ, bảng đối chiếu và ứng dụng. Các luận điểm sai và nguồn sai đã xác nhận được sửa trực tiếp, không khôi phục theo bản gốc.

## Phạm vi và kết quả

- 83 bài, đầy đủ bản Việt và Anh, giữ nguyên Content_ID để không đổi đường dẫn.
- Đối chiếu 480 URL cũ, gồm tài liệu và nguồn ảnh. HTTP: 211 trả 200, 187 trả 203/challenge, 70 trả 403, 10 trả 404, 2 trả 202. Đây là kết quả truy cập, không phải phép chấm chất lượng y khoa.
- Tra metadata của 187 PMID cũ qua Europe PMC; nhận 185 bản ghi. Hai bản ghi chưa trả về không được tự coi là hợp lệ.
- Xác nhận ít nhất 29 **bài có PMID nguồn chính không liên quan** bằng tên nghiên cứu thực tế; bảng chi tiết ở cuối báo cáo.
- Thay danh mục hoạt động bằng 82 nguồn: hướng dẫn cơ quan y tế, hội chuyên môn, tổng quan, nghiên cứu gốc và tài liệu hãng. Ghi rõ loại và phạm vi hỗ trợ. Không gọi mọi tài liệu hãng là nghiên cứu lâm sàng.
- Kiểm tra 82 URL nguồn hiện tại: 46 trả HTTP 200, 28 PubMed trả HTTP 203/challenge, 8 trả 403 từ bộ kiểm tra tự động; không có 404 trong danh mục mới. PMID được đối chiếu riêng với metadata, không dựa vào HTTP 203. Các nguồn bị chặn tự động được kiểm tra bằng trang chính thức hoặc nội dung chỉ mục tương ứng; không tuyên bố đã đọc toàn bộ full text của mọi nghiên cứu.
- Ở bước khôi phục bản dài, đã giữ 83 ảnh đầu bài và 22 sơ đồ gốc với chú thích sửa lại. Trạng thái ảnh hiện tại sau nghiên cứu theo phiên được ghi ở mục đợt 01 bên dưới. 61 hình tóm tắt dạng chữ đã được bỏ; các ý “hiểu đúng”, “thực hành” và “giới hạn” được giữ trong văn bản Việt/Anh của từng bài. Liên kết ảnh mở đúng asset; không tự gắn xác nhận tác giả hoặc giấy phép ngoài dự án.
- Cập nhật master Excel, hai roadmap và ba bản tải xuống trong website. Các sheet cũ được giữ, trường nội dung/nguồn được sửa; thêm bảng audit và nguồn.

## Nội dung đã sửa

1. Bỏ bảng trọng số điểm ngủ dùng chung cho nhiều hãng; phân biệt ước tính thiết bị với đa ký giấc ngủ. Không dùng một điểm để cấp phép tập nặng.
2. Bỏ suy diễn HRV/nhịp tim thành cortisol, testosterone, estrogen, serotonin, làm tổ hoặc xác nhận thai. Sửa cả metadata mapping vốn làm các cơ chế này trông như chỉ số đo được.
3. Bỏ lịch tập, chế độ ăn theo pha và các tỷ lệ hormone bắt buộc cho mọi người. Nêu rõ biến thiên cá nhân và giới hạn nghiên cứu.
4. Bỏ hướng dẫn tự dùng vi chất liều cao, mẹo khóa xuất tinh bảo đảm hiệu quả và lời hứa tăng testosterone. Nêu rõ vai trò thả lỏng sàn chậu, đánh giá nguyên nhân và kế hoạch có con khi bàn hormone.
5. Phân biệt tương quan với nhân quả trong nội dung sauna, quan hệ, giấc ngủ và dinh dưỡng sinh sản. Thử nghiệm nhỏ không được quy đổi thành tuổi sinh học hoặc tỷ lệ cải thiện chắc chắn.
6. Phát triển lại 83 bài song ngữ chuyên sâu dựa trên chủ đề và các điểm giải thích hữu ích của bản gốc. Mỗi bài có ít nhất ba phần giải thích cơ chế, tình huống minh họa riêng, bảng so sánh, thực hành và nguồn kèm phạm vi hỗ trợ. Phần nội dung chính trung bình khoảng 800 từ tiếng Anh và 1.400 từ tiếng Việt, không tính tài liệu tham khảo.
7. Giữ và đối chiếu nghiên cứu Dorey, Pastore, Esposito, LIFTMOR và hướng dẫn thiếu sắt; ghi rõ đối tượng, thiết kế, can thiệp và giới hạn suy rộng. Bài testosterone sau kiêng xuất tinh đã bị rút được dẫn chỉ để giải thích vì sao không dùng làm bằng chứng tăng hormone.
8. Bỏ nhãn “Clinical Editorial Board”, “hội đồng biên tập y khoa” và “hình xác thực 100%” chưa có thông tin chứng minh. Trạng thái duyệt bởi bác sĩ được ghi đúng là **chưa có xác nhận**.

## Hình ảnh

Ảnh và sơ đồ được xem bằng contact sheet cho toàn bộ thư viện cũ. Ví dụ không phù hợp:

- `LM_AC_02`: hình CO2/đáp ứng dịch trong hồi sức không giải thích WHOOP Day Strain.
- `WH_26`: hình thủ thuật sản khoa không hướng dẫn tập luyện thai kỳ.
- `MW_REL_01`: sơ đồ giải phẫu thần kinh không chứng minh tỷ lệ giao tiếp 5:1.
- `DM_SL_02`: công thức phân tử melatonin không giải thích nợ ngủ.

Các sơ đồ được giữ gồm khoảng R–R trên ECG, cấu trúc giấc ngủ, đo trao đổi khí, chuyển hóa sắt, sinh lý chu kỳ và giải phẫu sàn chậu. Chú thích phân biệt hình minh họa với dữ liệu của người đọc hoặc kết quả nghiên cứu. Ảnh đầu bài được khôi phục từ thư viện dự án gốc; việc giữ asset không tạo xác nhận mới về tác giả hoặc giấy phép ngoài dự án. Các hình sai chủ đề nêu trên được bỏ. Tóm tắt chỉ có chữ được trình bày trực tiếp trong nội dung bài, không xuất thành hình.

## Nghiên cứu ảnh theo phiên — đợt 01

Đợt đầu xử lý đúng 10 bài đầu tiên: LM_SL_01, LM_SL_02, DM_SL_01, DM_SL_02, LM_RC_01, LM_RC_02, DM_RC_01, DM_RC_02, LM_AC_01, LM_AC_02. Đã chọn 19 hình, ghi nguồn/tác giả/giấy phép và chú thích Việt/Anh theo nội dung thực sự nhìn thấy. Có 10 ảnh đầu bài và 9 hình trong bài. Hình đa ký N3 thay nhãn Stage 4 cũ; sơ đồ R–R không được gọi là dữ liệu của người đọc; ảnh Fitbit không được gọi là ảnh chụp AZM. Bài WHOOP chưa thêm hình thứ hai khi chưa có ứng viên đủ phù hợp và rõ quyền dùng.

Bộ mới dùng các ảnh Commons với giấy phép tương ứng và các ảnh Pexels được đối chiếu với trang ảnh/tác giả và giấy phép. Thông tin nguồn được lưu trong `data/image_selections.json`, sheet `Image_Register` của master Excel và hiển thị cạnh ảnh. 73 bài còn lại chưa được rà soát ảnh trong quy trình theo phiên; không gắn trạng thái hoàn tất cho các bài đó. Xem [tiến độ từng đợt](Image_Research_Progress.md) và [bộ ảnh đợt 01](Image_Research_Batch_01.html).

## File và khả năng kiểm tra lại

- `Master_Content_MVP`: 83 hàng nội dung đã sửa, danh mục nguồn JSON, giới hạn bằng chứng, ngày rà soát, trạng thái duyệt và URL bài.
- `Mapping_Matrix`: tiêu đề, chủ đề và nguồn chính khớp dữ liệu website.
- `HDSD_Data_Schema`: bỏ link mẫu và ví dụ PMID sai; phân biệt nguồn minh họa với nguồn nghiên cứu.
- `Editorial_Audit`: 83 hàng, lưu phát hiện và cách sửa, nguồn cũ/mới, tiêu đề thực của PMID cũ, giới hạn và đường dẫn bài.
- `Source_Register`: 82 nguồn, URL bấm được, loại nguồn và phạm vi hỗ trợ.
- `Link_Audit`: kết quả truy cập 480 URL cũ; các nguồn cũ trong sheet này được giữ làm bằng chứng audit, không phải nguồn đang dùng.
- Hai roadmap: sửa cả trường đang có và thêm `Reviewed_Content`, `Source_Register`. Women's roadmap có 30 hàng ánh xạ tới 28 ID khác nhau; hai cặp dùng chung bài là `LM_WH_01` và `DM_WH_03`, không phải 30 bài độc lập trong roadmap này.
- Bản cũ được giữ trong lịch sử Git và thư mục `audit/health-2026-10-26/before` ở workspace. Không có thay đổi xóa lịch sử.

## Kiểm tra kỹ thuật

- Kiểm tra 83 ID duy nhất, đủ nội dung Việt/Anh, nguồn chính thuộc danh mục đầy đủ, URL nghiên cứu khớp tên metadata, và các PMID sai xác nhận không quay lại bài tương ứng.
- Kiểm tra JSON/JS/Markdown/Excel/HTML khớp nhau, ba workbook local và bản tải xuống có nội dung byte giống nhau, toàn bộ ảnh đang dùng tồn tại, các hình tóm tắt chữ không còn được tham chiếu, ảnh có alt và đường dẫn HTML tương đối đúng.
- Chrome: mở toàn bộ 83 bài trong SPA ở cả hai ngôn ngữ; kiểm tra 109 ảnh đang dùng, 83 trang HTML, tìm kiếm, popup và chuyển ngôn ngữ. Kiểm tra mobile 390 px, không tràn ngang trang và không có lỗi JavaScript.
- Sửa lỗi CSS cũ thiếu quy tắc `.hidden`, khiến trang HTML hiện cả Việt lẫn Anh và phần bài mẫu trên trang chủ. Gắn sự kiện tìm kiếm trước khi tải dữ liệu để thao tác sớm không bị bỏ qua.
- Kiểm tra riêng MW_NUT_07 và toàn bộ dữ liệu/Excel: không có chú thích hay liên kết hình tóm tắt chữ. Thêm chặn hình chữ từ metadata cũ trong trang bài và popup; tải dữ liệu không dùng cache, đổi URL script và trả 404 cho ảnh đã xóa thay vì trả HTML trang blog. Chú thích chỉ hiển thị sau khi ảnh tải thành công; ảnh lỗi thì bỏ cả khung và chú thích trong trang bài, popup và trang HTML. Đã bổ sung kiểm tra ảnh bị chặn tải, hình chữ nhúng trong HTML cũ và giải mã ảnh thực tế.
- Kiểm tra cú pháp JavaScript và Git diff whitespace. Kiểm tra lại bản live sau khi đẩy lên Render được ghi riêng trong workspace.

## Giới hạn còn lại

Đây là rà soát biên tập dựa trên nguồn, không phải nghiên cứu hệ thống mới hoặc xác nhận của bác sĩ. Bản sửa là nội dung giáo dục chuyên sâu, không chẩn đoán người dùng hoặc kê điều trị cá nhân. Chưa có người duyệt lâm sàng được xác nhận; không thể gọi dữ liệu “chính xác 100%”. Nguồn có thể đổi sau ngày kiểm tra. Bản hiện tại đã thay thế bản tóm tắt ngắn của lần audit đầu. Khi cập nhật tiếp, chỉnh các tệp `data/longform_*` và nguồn tương ứng; không chạy lại các script bản nháp cũ vốn có trích dẫn và luận điểm chưa được kiểm tra.

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
| LM_MH_03 | [Influence of ionizing radiation on ovarian carcinoma SKOV- 3 xenografts in nude mice under hypoxic conditions.](https://pubmed.ncbi.nlm.nih.gov/24716983/) | [Dorey 2004](https://pubmed.ncbi.nlm.nih.gov/15527607/) |
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
