import cv2
import numpy as np
import time

cap = cv2.VideoCapture(0)

# Các biến hiệu ứng
scale = 0.0
alpha = 0.0

while True:
    success, image = cap.read()
    if not success: break
    
    image = cv2.flip(image, 1)
    h, w = image.shape[:2]
    
    # 1. Nhận diện màu da (Tăng ngưỡng sáng để lọc kỹ hơn)
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    lower_skin = np.array([0, 40, 80], dtype=np.uint8)
    upper_skin = np.array([20, 160, 255], dtype=np.uint8)
    mask = cv2.inRange(hsv, lower_skin, upper_skin)
    
    # Khử nhiễu mạnh
    mask = cv2.medianBlur(mask, 7)
    kernel = np.ones((5, 5), np.uint8)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    show_text = False
    
    if contours:
        # Lấy vùng da lớn nhất
        cnt = max(contours, key=cv2.contourArea)
        area = cv2.contourArea(cnt)
        
        # 2. LOGIC QUAN TRỌNG: Chỉ hiện khi xòe tay (diện tích đủ lớn)
        # Và chặn khuôn mặt (thường nằm ở trục giữa phía trên)
        if area > 22000: # Ngưỡng diện tích lớn hẳn để chỉ nhận bàn tay xòe gần cam
            M = cv2.moments(cnt)
            if M["m00"] != 0:
                cx = int(M["m10"] / M["m00"])
                cy = int(M["m01"] / M["m00"])
                
                # Chặn vùng khuôn mặt (thường ở giữa và phía trên)
                # Nếu tay không nằm quá gần mắt/miệng
                if cy > h * 0.35: 
                    show_text = True
                    
                    # --- HIỆU ỨNG BIẾN HÓA (FADE & ZOOM) ---
                    scale = min(scale + 0.1, 1.0)
                    alpha = min(alpha + 0.1, 1.0)
                    
                    # Nhịp đập ảo diệu
                    pulse = 1.0 + 0.05 * np.sin(time.time() * 8)
                    
                    if cx < w // 2:
                        text = "NGUYEN VU DUC THINH"
                        color = (0, 255, 127) # Xanh Neon
                    else:
                        text = "NEU"
                        color = (0, 0, 255) # Đỏ rực

                    # Tạo ảnh tạm để vẽ hiệu ứng mờ (Overlay)
                    overlay = image.copy()
                    
                    # Vẽ vòng tròn năng lượng tỏa lan
                    cv2.circle(overlay, (cx, cy), int(40 * scale * pulse), color, 2)
                    cv2.circle(overlay, (cx, cy), int(60 * scale * pulse), color, 1)

                    # Vẽ chữ bám theo lòng bàn tay
                    font = cv2.FONT_HERSHEY_TRIPLEX
                    text_size = scale * pulse
                    # Bóng chữ
                    cv2.putText(overlay, text, (cx - 110, cy - 40), font, text_size, (0, 0, 0), 4)
                    # Chữ chính
                    cv2.putText(overlay, text, (cx - 110, cy - 40), font, text_size, color, 2)
                    
                    # Áp dụng hiệu ứng Fade-in
                    cv2.addWeighted(overlay, alpha, image, 1 - alpha, 0, image)

    # Nếu nắm tay (area nhỏ lại) hoặc không có tay, reset ngay lập tức
    if not show_text:
        scale = 0.0
        alpha = 0.0

    # Đường kẻ phân chia mờ
    cv2.line(image, (w//2, 50), (w//2, h-50), (255, 255, 255), 1)
    
    cv2.imshow('Xoe Tay Bien Hoa - Thinh NEU', image)
    if cv2.waitKey(1) & 0xFF == ord('q'): break

cap.release()
cv2.destroyAllWindows()
