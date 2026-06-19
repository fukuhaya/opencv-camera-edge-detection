import cv2


def main():
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("カメラを開けませんでした。")
        return

    while True:
        ret, frame = cap.read()

        if not ret:
            print("フレームを取得できませんでした。")
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        edges = cv2.Canny(gray, 100, 200)

        cv2.imshow("Original", frame)
        cv2.imshow("Canny Edge Detection", edges)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()