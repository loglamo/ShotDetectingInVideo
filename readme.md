# Read me


Chương trình để phát hiện các Shots trong một Video ngắn sử dụng trích chọn đặc trưng cục bộ SIFT

Link video sử dụng [DNA teaser](https://www.youtube.com/watch?v=g_wuoInNyAI)

Hướng giải quyết:

- Bước 1: Từ video tách lấy các frames

- Bước 2: Vì số lượng Frames là rất lớn, trong khi theo lí thuyết phải trích chọn đặc trưng của các frames, và từ các đặc trưng trích được đem đối sánh giữa 2 frames liền kề, để đưa ra kết luận có phải là shot boundary hay không, việc làm này sẽ tốn rất hiều thời gian, cho nên có một giải pháp dựa trên paper "A Divide-And-Rule Scheme For Shot Boundary Detection Based on SIFT" của Jun Li 1 , Youdong Ding 1 , Yunyu Shi 1 , Wei Li 2.

Tức là: Trước hết, sẽ đối sánh các frame về màu sắc trước. Vì khi các shots thay đổi, màu sắc phần lớn cũng sẽ thay đổi. Sẽ lưu lại các cặp frames mà tại đó việc thay đổi màu sắc được ghi nhận là thay đổi lớn ( trên một ngưỡng nào đó). Từ các cặp frames(frame_a, frame_b) ( candidates),giữa 2 frames này có thể là Shot boundary,  sẽ lấy 3 frames liền trước frame_a, và 3 frames sau frame_b. Tình đặc trưng SIFT của các frames này, cùng với đó là Match giữa các frames. Làm bước này để phân loại boundary, là cut transition, hay fade transition, wide transition, .... chương trình này chỉ phát hiện 2 trường hợp trước. Xảy ra cut transition khi match(frame_a, frame_b) là thấp nhất trong tập match. Xảy ra fade transition khi match giữa các frames giảm dần sau đó lại tăng lên.

- Bước 3: Sau khi đã xác định được vị trí boundary đưa các frames về cùng shot

Chi tiết các files:

- file FilterFrames.py, đây là file extract video ra các frames, lưu các frames vào folder frames

- file ColorExtract.py, đây là file để phát hiện các candidate shot boundary dựa trên sự sai khác về màu sắc

- ShotsExtract.py, là file xác đinh shot boundary, đưa các frames về cùng shot lưu trong folder shots

LƯU Ý:

OpenCV mặc định không hỗ trợ module trích chọn đặc trưng SIFT/SURF, vì vậy khi cài đặt OpenCV cần cài đặt cùng thư viện  opencv_contrib, có thể theo [hướng dẫn trên medium](https://medium.com/@debugvn/installing-opencv-3-3-0-on-ubuntu-16-04-lts-7db376f93961).

Đọc về feature matching tại [matching](https://docs.opencv.org/3.0-beta/doc/py_tutorials/py_feature2d/py_matcher/py_matcher.html)

Trích chọn theo color tại [color](https://docs.opencv.org/3.1.0/dd/d0d/tutorial_py_2d_histogram.html)

end.

