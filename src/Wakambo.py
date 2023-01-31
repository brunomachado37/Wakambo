from fer import FER
import cv2

class Wakambo:

    def __init__(self, numberOfEmotions: int = 1) -> None:

        self.detector = FER()
        self.numberOfEmotions = numberOfEmotions


    def run(self) -> None:

        vid = cv2.VideoCapture(0)

        print("\nPress 'q' to quit\n")
  
        while(True):

            _, frame = vid.read()

            faces = self.detector.detect_emotions(frame)

            for face in faces:

                cv2.rectangle(frame, (face["box"][0], face["box"][1]), (face["box"][0] + face["box"][2], face["box"][1] + face["box"][3]), (128, 128, 0), 4)

                ordered = sorted(face["emotions"], key = face["emotions"].get, reverse=True)
                
                for i in range(self.numberOfEmotions):
                    frame = cv2.putText(frame, f"{ordered[i]}: {face['emotions'][ordered[i]]:.0%}", (face["box"][0], face["box"][1] + face["box"][3] + 30 * (i + 1)), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 1, cv2.LINE_AA)
        
            cv2.imshow('frame', frame)
            
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        

        vid.release()

        cv2.destroyAllWindows()