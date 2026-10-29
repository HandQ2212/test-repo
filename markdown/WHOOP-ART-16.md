# Ngủ phục hồi: hiểu số giờ Deep, REM và tỷ lệ trong đêm

Restorative Sleep, thường được gọi là thời gian ngủ phục hồi, là cách nhóm **ngủ sâu và REM** trên báo cáo giấc ngủ. Trong &lt;Tên App/&gt;, phần này giúp bạn nhìn hai giai đoạn đó bằng số giờ và tỷ lệ trong tổng thời gian ngủ.

Tên gọi “phục hồi” không có nghĩa các giai đoạn còn lại vô ích, cũng không có nghĩa tỷ lệ càng cao thì đêm càng tốt. Muốn đọc đúng, cần biết từng phần là gì, mẫu số của tỷ lệ và mức độ thiết bị thực sự quan sát được.

## Một đêm ngủ không chỉ có ngủ sâu

Giấc ngủ gồm hai nhóm lớn: NREM và REM. NREM có các giai đoạn N1, N2 và N3. N1 là chuyển tiếp từ thức sang ngủ; N2 là một phần bình thường của giấc ngủ; N3 thường được gọi là ngủ sâu hoặc ngủ sóng chậm. REM có hoạt động não và chuyển động mắt đặc trưng. [S20](https://www.nhlbi.nih.gov/health/sleep/stages-of-sleep)

Các giai đoạn thay nhau trong đêm. Ngủ sâu thường tập trung nhiều hơn ở phần đầu, còn REM thường nhiều hơn về phía sau. Không có yêu cầu một đêm phải là một khối ngủ sâu liên tục, và thức ngắn giữa các chu kỳ có thể xảy ra. [S20](https://www.nhlbi.nih.gov/health/sleep/stages-of-sleep)

Vì vậy, một báo cáo có nhiều phần Core hoặc Light không tự có nghĩa bạn đã ngủ “sai”. Trong dữ liệu Apple, Core bao gồm nhóm ngủ nông hoặc trung gian, còn Deep tương ứng nhóm ngủ sâu và REM được ghi riêng. [S77](https://developer.apple.com/documentation/healthkit/hkcategoryvaluesleepanalysis)

## Số giờ ngủ phục hồi được tính ra sao?

Cách nhóm trên báo cáo là:

**Thời gian ngủ phục hồi = thời gian Deep + thời gian REM.**

Ví dụ minh họa, Deep được ghi là một giờ và REM là hai giờ. Tổng nhóm này là ba giờ. Đó là phép cộng hai phần đã được thiết bị phân loại, không phải một phép đo độc lập cho biết cơ thể đã sửa chữa được bao nhiêu mô.

Nguồn dữ liệu phải có thông tin giai đoạn thì mới mô tả được hai phần này. Một nhật ký chỉ ghi giờ lên giường và thức dậy không tự cho biết Deep hoặc REM. Thiếu giai đoạn trên màn hình không có nghĩa bạn không trải qua giai đoạn đó khi ngủ.

## Tỷ lệ dùng tổng thời gian ngủ làm mẫu số

**Tỷ lệ ngủ phục hồi = (Deep + REM) ÷ tổng thời gian ngủ × 100%.**

Mẫu số là thời gian được ghi là ngủ, không phải toàn bộ thời gian trên giường. Nếu có các khoảng thức trong đêm, chúng không được cộng vào tổng ngủ chỉ để làm mẫu số lớn hơn.

Giữ tổng Deep và REM là ba giờ, so hai đêm giả định:

| Phần dữ liệu | Đêm A | Đêm B |
|---|---|---|
| Tổng thời gian ngủ | 8 giờ | 6 giờ |
| Deep + REM | 3 giờ | 3 giờ |
| Tỷ lệ | 37,5% | 50% |

Đêm B có tỷ lệ cao hơn vì tổng ngủ ngắn hơn, không phải vì số giờ Deep cộng REM tăng. Vì vậy, không thể chọn đêm B là đêm phục hồi tốt hơn chỉ dựa vào hai phần trăm.

Ví dụ này cũng cho thấy vì sao nên xem số giờ và tỷ lệ cạnh nhau. Phần trăm là mối quan hệ giữa hai đại lượng; nó có thể đổi do tử số, mẫu số hoặc cả hai.

## Vì sao không nên cố giảm ngủ nông để tăng tỷ lệ?

N1 và N2 thuộc cấu trúc ngủ bình thường. Nhóm Deep + REM giúp tóm tắt một góc nhìn, không phải bảng xếp hạng cho rằng các phút còn lại không có giá trị. Ngủ hỗ trợ hoạt động não và nhiều chức năng sức khỏe thông qua cả một đêm, không chỉ một ô dữ liệu. [S20](https://www.nhlbi.nih.gov/health/sleep/stages-of-sleep) [S67](https://www.nhlbi.nih.gov/health/sleep/why-sleep-important)

Cắt ngắn thời gian ngủ để làm tỷ lệ một nhóm tăng cũng không có nghĩa giúp bạn tốt hơn. Đặc biệt, dậy sớm hơn nhiều có thể làm mất một phần cuối đêm vốn thường có nhiều REM. Điều có ích hơn là dành cơ hội ngủ phù hợp và xem mức tỉnh táo ban ngày.

Bạn không cần đặt mục tiêu Deep hoặc REM bằng một con số của người khác. Tuổi và cấu trúc ngủ thay đổi theo thời gian; cùng một người cũng có thể có các đêm khác nhau. [S20](https://www.nhlbi.nih.gov/health/sleep/stages-of-sleep)

## Thiết bị biết giai đoạn bằng cách nào?

Khảo sát giấc ngủ trong cơ sở y tế có thể ghi hoạt động não, mắt và cơ để phân loại trạng thái. Thiết bị đeo tiêu dùng thường suy từ chuyển động và tín hiệu sinh lý gián tiếp. Hai cách có bộ thông tin khác nhau, nên kết quả không tương đương mọi mặt. [S75](https://pubmed.ncbi.nlm.nih.gov/34314344/)

Một thiết bị có thể ước tính thời gian ngủ khá hữu ích nhưng vẫn phân loại nhầm giai đoạn. Không lấy chất lượng nhận ra “ngủ hay thức” để bảo đảm cùng chất lượng cho từng phút Deep hoặc REM.

Dữ liệu có nhãn “ngủ, chưa xác định giai đoạn” cũng khác dữ liệu thức. Nó cho biết có thông tin về ngủ nhưng chưa phân loại chi tiết. Trong Apple Sức khỏe, trạng thái này được phân biệt với Core, Deep, REM và Awake. [S77](https://developer.apple.com/documentation/healthkit/hkcategoryvaluesleepanalysis)

## Khi thấy một đêm khác thường

Đầu tiên, nhìn tổng ngủ có ngắn hơn, bản ghi có gián đoạn hoặc cách đeo có đổi không. Một phần trăm mới không tự chỉ ra bạn đang thiếu một giai đoạn cụ thể hoặc có vấn đề thần kinh.

Sau đó, đặt cạnh trải nghiệm. Bạn có tỉnh táo hơn không, có buồn ngủ trong công việc hoặc ngáy kèm ngưng thở được người bên cạnh nhận thấy không? Một biểu đồ đẹp không phủ định những khó khăn này, còn một đêm có tỷ lệ thấp chưa đủ để tự chẩn đoán.

Nếu theo dõi, so nhiều đêm có cách ghi tương đối nhất quán. Ghi ngắn những thay đổi như giờ ngủ, lịch làm việc hoặc bệnh gần đây sẽ giúp bạn giải thích xu hướng rõ hơn thay vì chỉ so màu.

## Ưu tiên điều có thể hỗ trợ giấc ngủ thực tế

Hãy dành thời gian ngủ phù hợp với hoàn cảnh, giữ một phần lịch ổn định và tạo môi trường giúp ngủ dễ hơn. Những việc này có mục tiêu rõ hơn việc mua một sản phẩm với lời hứa làm tăng riêng một giai đoạn. [S74](https://www.nhlbi.nih.gov/health/sleep-deprivation/healthy-sleep-habits)

Nếu giấc ngủ không hồi phục kéo dài, ngáy kèm ngưng thở hoặc buồn ngủ ảnh hưởng an toàn, cần được đánh giá. Công nghệ theo dõi có thể bổ sung lịch sử cho cuộc trao đổi, nhưng không thay việc chẩn đoán và điều trị rối loạn ngủ. [S75](https://pubmed.ncbi.nlm.nih.gov/34314344/)

Khi đọc &lt;Tên App/&gt;, kết hợp ba phần: tổng thời gian ngủ, số giờ và tỷ lệ Deep + REM, cùng cảm nhận ban ngày. Đó là cách sử dụng chỉ số này có ích mà không biến mỗi đêm thành một cuộc thi tỷ lệ.

## Nguồn tham khảo và phạm vi hỗ trợ

- **S20** —  [NINDS: kiến thức về giấc ngủ và các giai đoạn ngủ](https://www.nhlbi.nih.gov/health/sleep/stages-of-sleep). Phạm vi tài liệu: NREM gồm N1, N2, N3; REM; N1 là ngủ, không phải thức.
- **S77** —  [Apple: thời gian trên giường, ngủ, thức và các giai đoạn](https://developer.apple.com/documentation/healthkit/hkcategoryvaluesleepanalysis). Phạm vi tài liệu: In-bed, awake, core, deep,REM và asleep-unspecified; dữ liệu awake giữa các mẫu ngủ và giới hạn diễn giải latency/số lần thức.
- **S67** —  [NHLBI: vai trò của giấc ngủ đối với não và cơ thể](https://www.nhlbi.nih.gov/health/sleep/why-sleep-important). Phạm vi tài liệu: Giấc ngủ hỗ trợ hoạt động não, tim mạch và sức khỏe; ngủ không đủ ảnh hưởng chú ý và hoạt động ban ngày.
- **S75** — Schutte-Rodin S, Deak MC, Khosla S, et al. J Clin Sleep Med. 2021. [AASM: đánh giá công nghệ theo dõi giấc ngủ](https://pubmed.ncbi.nlm.nih.gov/34314344/). PMID 34314344. Phạm vi tài liệu: Phân biệt công nghệ ngủ tiêu dùng và đánh giá lâm sàng; xác thực từng kết quả, giới hạn suy đoán ngủ/thức/giai đoạn.
- **S74** —  [NHLBI: thói quen hỗ trợ ngủ và lịch làm ca](https://www.nhlbi.nih.gov/health/sleep-deprivation/healthy-sleep-habits). Phạm vi tài liệu: Lịch ngủ đều, cơ hội ngủ, môi trường và caffeine; hỗ trợ người làmca.

> Bài biên soạn độc lập bởi Pulse & Vitality. Nội dung chỉnh ngày 29/10/2026; nguồn đối chiếu 2026-10-26. Liên kết được đặt tên theo chủ đề; tên tài liệu gốc và đơn vị phát hành có trên trang nguồn.
