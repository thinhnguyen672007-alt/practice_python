
import cv2
import mediapipe as mp

# Khởi tạo MediaPipe Hands
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
hands = mp_hands.Hands(
    min_detection_confidence=0.7, 
    min_tracking_confidence=0.7
)

# Mở webcam
cap = cv2.VideoCapture(0)


def detect_hand_side(hand_landmarks, image_width):
    """Phát hiện tay trái hay tay phải"""
    wrist = hand_landmarks.landmark[mp_hands.HandLandmark.WRIST]
    thumb_tip = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]
    
    if thumb_tip.x < wrist.x:
        return "RIGHT"
    else:
        return "LEFT"


def is_hand_raised(hand_landmarks):
    """Kiểm tra xem tay có được giơ lên không"""
    wrist_y = hand_landmarks.landmark[mp_hands.HandLandmark.WRIST].y
    middle_y = hand_landmarks.landmark[
        mp_hands.HandLandmark.MIDDLE_FINGER_TIP
    ].y
    
    return middle_y < wrist_y


while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    frame = cv2.flip(frame, 1)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb_frame)
    
    display_text = ""
    
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(
                frame, 
                hand_landmarks, 
                mp_hands.HAND_CONNECTIONS
            )
            
            if is_hand_raised(hand_landmarks):
                hand_side = detect_hand_side(
                    hand_landmarks, 
                    frame.shape[1]
                )
                
                if hand_side == "LEFT":
                    display_text = "Nguyen Vu Duc Thinh"
                elif hand_side == "RIGHT":
                    display_text = "NEU"
    
    if display_text:
        size = cv2.getTextSize(
            display_text, 
            cv2.FONT_HERSHEY_SIMPLEX, 
            2, 
            3
        )
        text_width, text_height = size[0]
        
        cv2.rectangle(
            frame, 
            (40, 50), 
            (60 + text_width, 90 + text_height), 
            (0, 0, 0), 
            -1
        ).venv
        
        cv2.putText(
            frame, 
            display_text, 
            (50, 100), 
            cv2.FONT_HERSHEY_SIMPLEX, 
            2, 
            (0, 255, 255), 
            3
        )
    
    cv2.imshow('Hand Gesture Recognition', frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
hands.close()